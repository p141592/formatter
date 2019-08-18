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

    def __init__(self, document=None):
        self.files = []

        self.db = DB()
        self.document = Document(self.check_file(document))
        self.prev_line = None  # Ссылка на предидущий объект
        self.line = None
        self.block = None

        self.offset = 1
        self.position = 0 # Индекс в списке children родителя

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
        return bool(reg.match(line.source))

    def read_line(self, line):
        self.line = self.document.create_child(child_type=Line, offset=self.offset, source=line or None)
        self.line.format_sign = self.check_special_symbols(self.line)
        self.offset += 1
        return self.line

    def read_document(self):
        with self.document.file as f:
            for line in f.readlines():
                _line = self.read_line(line.strip('\n'))

        return self.document
