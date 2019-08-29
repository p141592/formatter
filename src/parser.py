import os
import re


from exceptions import PathException
from tree import BaseNodeDBSerializator, BaseTree
from src.tree.nodes import Line, Root


class Parser:
    """Инструкции для преобразования исходного документа в Дерево"""
    STATUS = ('idle', 'parsing', 'raw', 'formatting', 'done')
    def __init__(self, source):
        """Принимает на вход объект Source и из него формирует Document"""
        self.root = Root()
        self.status = None
        self.document = None
        self.prev_line = None  # Ссылка на предидущий объект
        self.line = None
        self.block = None
        self.position = 0
        self.line_number = 1

    def get_status(self):
        if self.status is None:
            return
        return self.STATUS[self.status]

    @staticmethod
    def check_file(path):
        if os.path.exists(path):
            return path
        raise PathException

    def read_line(self, line):
        self.line = self.document.create_child(child_type=Line, line_number=self.line_number, content=line or None)
        self.line_number += 1
        return self.line

    def read_document(self, file):
        try:
            for line in f.readlines():
                _line = self.read_line(line.strip('\n'))
        except UnicodeDecodeError:
            print(f'Ошибка при чтении файла {self.document.path}')

        return self.document

    def load(self, source):
        """Формирование дерева"""
        pass

    def parsing(self, formatter):
        """Применение правил формата"""
        pass
