import uuid

from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declared_attr


class BaseTree:
    """
    Базовый класс нод.
    Управляет связями между нодами, добавлением элементов, преобразованием, и вообще всем.
    """
    def __init__(self, *args, content=None, **kwargs):
        self.children = []
        self.parent = None
        self.content = content # Готовое значение

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


class BaseNode:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(UUID, default=uuid.uuid1, primary_key=True)