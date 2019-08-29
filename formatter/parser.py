import os

from exceptions import PathException
from tree.nodes import Line, Root


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

    def read_document(self, file):
        try:
            for index, line in enumerate(file.readlines()):
                self.document.create_child(child_type=Line, line_number=index, content=line or None)
        except UnicodeDecodeError:
            print(f'Ошибка при чтении файла {self.document.path}')

        return self.document

    def load(self, source):
        """Формирование дерева"""
        with source as document:
            self.read_document(document)
        return self.root

    def parsing(self, formatter):
        """Применение правил формата"""
        pass
