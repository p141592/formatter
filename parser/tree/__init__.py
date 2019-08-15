from parser.db import DB


class BaseTree:
    """
    Базовый класс нод.
    Управляет связями между нодами, добавлением элементов, преобразованием, и вообще всем.
    """
    DB_FIELDS = ('type', 'path', 'filename', 'offset', 'source', 'content', 'format_sign', 'parent', )

    def __init__(self, *args, content=None, **kwargs):
        self.children = []
        self.parent = None
        self.content = content # Готовое значение
        self.db = DB()

    def __str__(self):
        return self.content or self.source or ''

    def get_parent(self, parent_type):
        """Найти родителя заданного типа"""
        if self.type == parent_type:
            return self

        if self.parent:
            return self.parent.get_parent(parent_type)

    def append(self, node):
        """Добавить ноду в этот корень"""
        node.parent = self
        self.children.append(node)

    def to_db(self):
        return filter(lambda x: x if x in BaseTree.DB_FIELDS else None, self.__dict__)
