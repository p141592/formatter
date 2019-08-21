import datetime
import uuid

from typing import Generator

from marshmallow import fields, Schema
from sqlalchemy import Column, TEXT, DateTime, ForeignKey, String, Integer, Boolean, Table, exists
from sqlalchemy.dialects.postgresql import UUID

from parser.db import DB

class BaseTree:
    """
    Базовый класс нод.
    Управляет связями между нодами, добавлением элементов, преобразованием, и вообще всем.
    """
    def __init__(self, *args, position=0, **kwargs):
        self.id =  kwargs.get('id', uuid.uuid1()) # Ключ
        self.type = self.__class__.__name__
        self.db = None # Объект общения с базой
        self.position = position # Позиция в списке children у родителя
        self.children = [] # Список детей
        self.parent = None # Ссылка на родителя
        self.children_type = None # Стандартный тип детей
        self._previous = None # Ссылка на предидущий объект у родителя
        self._next = None # Ссылка на следующий объект родителя
        self.content = None
        self.filename = None
        self.path = None

    def __str__(self):
        return self.content or ''

    def __len__(self):
        return sum(map(len, self.children)) + 1

    def get_parent(self, parent_type=None):
        """Найти родителя заданного типа"""
        if parent_type and self.type == parent_type:
            return self

        if self.parent:
            return self.parent.get_parent(parent_type)

    def create_child(self, *args, child_type=None, **kwargs):
        """Создать ребенка"""
        kwargs['position'] = len(self.children)
        if child_type:
            _child = child_type(*args, **kwargs)
        else:
            _child = self.children_type(*args, **kwargs)
        self._append(_child)
        return _child

    def _append(self, node):
        """Добавить ноду в этот корень"""
        node.parent = self
        self.children.append(node)

    @property
    def previous(self):
        """Предидущий объект того же типа"""
        if not self._previous and self.parent.children[-1] != self.position:
            self._previous = self.parent.children[self.position-1]
        return self._previous

    @property
    def next(self):
        """Следующий объект того же типа"""
        if not self._next and self.position != 0:
            self._next = self.parent.children[self.position - 1]
        return self._next

    def get_db(self):
        """Найти db объект у родителей или создать"""
        if self.db:
            return self.db

        parent = self.get_parent()
        if not parent:
            self.db = DB()
            return self.db

        return parent.get_db()

    # Вставка данных в базу
    def db_collect_models(self) -> Generator:
        """Генератор для получения все элементов дерева список"""
        yield self.to_db()

        for child in self.children:
            yield from child.db_collect_models()

    def db_insert(self):
        "Коммит себя и всех детей в базу"
        self.db = self.get_db()
        self.db.commit(self.db_collect_models())

    def to_db(self):
        """Собрать все ключи для таблици в базе и вернуть BaseNodeDB объект"""
        serializator = BaseNodeDBSerializator().dump(self)
        return BaseNodeDB(
            **serializator.data
        )

    # Получение данных из базы
    def db_get_children(self):
        """Выполнить запрос на получение ID элементов, у которых я родитель"""
        table = BaseNodeDB
        return self.get_db().session.query(table).filter(table.parent==self.id).order_by('position').all()

    @classmethod
    def load_object(cls, id, db=None):
        """Получить дерево начиная с ноды с этим ID"""
        # Получить элемент из базы
        element = db.session.query(BaseNodeDB).filter(BaseNodeDB.id == id).first()
        # Получить класс, который нужно объявить по типу
        node_class = list(filter(lambda x: x.__name__ == element.type, BaseTree.__subclasses__()))
        node_class = node_class[0] if node_class else None
        # Получить объект дерева
        serializer =  BaseNodeDBSerializator(many=False).load(element.__dict__)
        if serializer.errors:
            raise ValueError(serializer.errors)
        object = node_class(**serializer.data)
        list(
            map(
                lambda x: cls.load_object(x.id, db=db),
                object.db_get_children()
            )
        )
        return object

class BaseNodeDB(DB.BASE):
    """Таблица для сохранения элементов дерева в базу"""
    __tablename__ = "node"

    id = Column(UUID(as_uuid=True), primary_key=True)
    type = Column(String(30))

    path = Column(String(100))
    filename = Column(String(50))
    line_number = Column(Integer, nullable=True)
    content = Column(TEXT, nullable=True)

    format_sign = Column(Boolean)
    parent = Column(UUID(as_uuid=True), ForeignKey('node.id'), nullable=True)
    position = Column(Integer)

    created_date = Column(DateTime, default=datetime.datetime.now)

class BaseNodeDBSerializator(Schema):
    """Сериализатор объекта из базы и в базу
    - Преобразование parent.id в parent
    """
    id = fields.UUID()
    type = fields.String() # Тип объекта строкой
    format_sign = fields.Boolean(allow_none=True) # Признак формата в строке Boolean
    parent = fields.Method("get_parent", deserialize="load_parent", allow_none=True) # ForeignKey на родителя объекта
    position = fields.Integer() # Позиция в списке children у родителя
    path = fields.String(allow_none=True) # Полный путь до файла
    filename = fields.String(allow_none=True) # Название файла
    line_number = fields.Integer(allow_none=True) # Номер строки
    content = fields.String(allow_none=True) # Содержит исходную строку целиком

    def get_parent(self, obj):
        return obj.parent.id

    def load_parent(self, value):
        return value
