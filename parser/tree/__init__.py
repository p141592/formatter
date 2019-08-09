import datetime
import uuid

from sqlalchemy import Column, TEXT, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from parser import Base


class BaseTree(Base):
    """
    Базовый класс нод.
    Управляет связями между нодами, добавлением элементов, преобразованием, и вообще всем.
    """
    __tablename__ = 'node'

    id = Column(UUID, default=uuid.uuid1, primary_key=True)
    type = Column(String(30))
    content = Column(TEXT)
    created_date = Column(DateTime, default=datetime.datetime.now)
    parent = Column(UUID, ForeignKey('node.id'))

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
