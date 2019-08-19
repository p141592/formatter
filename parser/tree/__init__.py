from parser.db import DB


class BaseTree:
    """
    Базовый класс нод.
    Управляет связями между нодами, добавлением элементов, преобразованием, и вообще всем.
    """
    DB_FIELDS = (
        # Описание объекта
        'type', # Тип объекта строкой
        'format_sign', # Признак формата в строке Boolean
        
        # Связи объекта
        'parent', # ForeignKey на родителя объекта
        'children', # ManyToMany список объектов
        'previous', # Вычислямое поле предидущего элемента в списке родителя
        'next', # Вычисляемое поле, следующий элемент
        'position', # Позиция в списке children у родителя

        # Сохранение информации источника
        'path', # Полный путь до файла
        'filename', # Название файла

        # Контект и информация по нему
        'line_number', # Номер строки
        'content' # Содержит исходную строку целиком
    )

    def __init__(self, *args, **kwargs):
        self.position = 0
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

    def to_db(self):
        return filter(lambda x: self.__dict__.get(x) if x in BaseTree.DB_FIELDS else None, self.__dict__)
