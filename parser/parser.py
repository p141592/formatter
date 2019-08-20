import os
import re

from parser.db import DB
from .exceptions import PathException
from .tree.nodes import Document, Line


class Parser:
    """
    Преобразование файла в объект Document
    """
    FILES_LENGTH = 0

    def __init__(self, document=None, position=None):
        self.files = []

        self.document = Document(self.check_file(document), position=position)
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

    def read_document(self):
        with self.document.file as f:
            try:
                for line in f.readlines():
                    _line = self.read_line(line.strip('\n'))
            except UnicodeDecodeError:
                print(f'Ошибка при чтении файла {self.document.path}')

        return self.document
