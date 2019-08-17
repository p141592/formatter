import os
import re

from .exceptions import PathException
from .tree.nodes import Document, RawLine, Block


class Parser:
    """
    Преобразование файла в объект Document
    """
    FILES_LENGTH = 0

    def __init__(self, document=None):
        self.files = []

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
        if line.type == 'BLANK':
            return False

        reg = re.compile('[\W+^]+')
        return bool(reg.match(line.source))

    def block_magic(func):
        def magic(self, line, *args, **kwargs):
            if line and not self.block:
                self.block = Block()
                self.document.append(self.block)

            if not line:
                self.block = None

            return func(self, line, *args, **kwargs)
        return magic

    @block_magic
    def read_line(self, line):
        self.line = RawLine(offset=self.offset, source=line or None)
        self.line.format_sign = self.check_special_symbols(line)
        self.offset += 1
        return self.line

    def read_document(self):
        with self.document.file as f:
            for line in f.readlines():
                _line = self.read_line(line.strip('\n'))
                if _line:
                    self.document.append(_line)

        return self.document
