import datetime
import uuid

from sqlalchemy import Column, TEXT, DateTime, ForeignKey, String, Integer, Boolean, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from parser.db import DB

#_db = DB()

class BaseTree:
    """
    Базовый класс нод.
    Управляет связями между нодами, добавлением элементов, преобразованием, и вообще всем.
    """
    DB_FIELDS = (
        # Описание объекта
        'id',
        'type', # Тип объекта строкой
        'format_sign', # Признак формата в строке Boolean
        
        # Связи объекта
        'parent', # ForeignKey на родителя объекта
        #'children', # ManyToMany список объектов
        #'previous', # Вычислямое поле предидущего элемента в списке родителя
        #'next', # Вычисляемое поле, следующий элемент
        'position', # Позиция в списке children у родителя

        # Сохранение информации источника
        'path', # Полный путь до файла
        'filename', # Название файла

        # Контект и информация по нему
        'line_number', # Номер строки
        'content' # Содержит исходную строку целиком
    )

    def __init__(self, *args, position=0, **kwargs):
        self.id = uuid.uuid1()
        self.db = DB() # TODO: Вынести из объявления класса. Это замедляет сильно процесс
        self.position = position # Позиция в списке children у родителя
        self.children = []
        self.parent = None
        self.children_type = None
        self._previous = None
        self._next = None

    def __str__(self):
        return self.content or ''

    def get_parent(self, parent_type):
        """Найти родителя заданного типа"""
        if self.type == parent_type:
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

    def db_flush(self):
        self.db_insert() # insert себя в базу
        for _child in self.children:
            _child.db_flush() # Добавление всех детей

    def db_insert(self):
        self.db.insert(self.to_db())

    def to_db(self):
        """Собрать все ключи для таблици в базе и вернуть BaseNodeDB объект"""
        _tmp = {k: v for k, v in self.__dict__.items() if k in self.DB_FIELDS}
        if 'parent' in _tmp:
            _tmp['parent_id'] = _tmp['parent'].id if _tmp['parent'] else None
            _tmp.pop('parent')
        return BaseNodeDB(
            **_tmp
        )

class BaseNodeDB(DB.BASE):
    """Таблица для сохранения элементов дерева в базу"""
    __tablename__ = "node"

    id = Column(UUID(as_uuid=True), default=uuid.uuid1, primary_key=True)

    type = Column(String(30))
    format_sign = Column(Boolean)

    parent_id = Column(UUID(as_uuid=True), ForeignKey('node.id'), nullable=True)
    #parent = relationship(lambda: BaseNodeDB, remote_side=id, backref='node')
    position = Column(Integer, nullable=True)

    path = Column(String(100), comment='Путь до файла, который был объявлени при создании документа')
    filename = Column(String(50), comment='Название документа')

    line_number = Column(Integer, nullable=True)
    content = Column(TEXT, nullable=True)

    created_date = Column(DateTime, default=datetime.datetime.now)
