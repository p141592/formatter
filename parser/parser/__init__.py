import os
import re

from parser.db import DB
from parser.tree import BaseNodeDB, BaseNodeDBSerializator, BaseTree
from .exceptions import PathException
from .tree.nodes import Document, Line


class BaseParser:
    """
    Объект, содержащий инструкции для преобразования исходного документа в Дерево
    - Разбор из файла
    - Получение дерева из базы
    """
    def __init__(self, document=None, position=None):
        """Принимает на вход объект Source и из него формирует Document"""
        self.files = []

        self.document = Document(file=self.check_file(document), position=position)
        self.prev_line = None  # Ссылка на предидущий объект
        self.line = None
        self.block = None
        self.position = 0
        self.line_number = 1

    @staticmethod
    def check_file(path):
        if os.path.exists(path):
            return path
        raise PathException

    @staticmethod
    def check_special_symbols(line):
        if not line:
            return False

        reg = re.compile('[\W+^]+')
        return bool(reg.match(line.content))

    def read_line(self, line):
        self.line = self.document.create_child(child_type=Line, line_number=self.line_number, content=line or None)
        self.line.format_sign = self.check_special_symbols(self.line)
        self.line_number += 1
        return self.line

    def read_document(self, source):
        with source as f:
            try:
                for line in f.readlines():
                    _line = self.read_line(line.strip('\n'))
            except UnicodeDecodeError:
                print(f'Ошибка при чтении файла {self.document.path}')

        return self.document

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
