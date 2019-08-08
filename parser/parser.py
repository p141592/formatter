import os

from parser.exceptions import PathException
from parser.tree.nodes import Document, Line, Term, Block


class Parser:
    """
    Преобразование файла в объект Document
    """
    FILES_LENGTH = 0

    def __init__(self, document=None):
        self.document = Document(self.check_file(document))
        self.line = None
        self.block = None
        self.offset = 1
        self.files = []

    def check_file(self, path):
        if os.path.exists(path):
            return path
        raise PathException

    def read_word(self, word):
        return Term(content=word)

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
        if line:
            self.line = Line(offset=self.offset, source=line)

            for _word in line.strip().split(' '):
                self.line.append(self.read_word(_word))

            self.offset += 1
            return self.line

    def read_document(self):
        with self.document.file as f:
            for line in f.readlines():
                _line = self.read_line(line.strip('\n'))
                if _line:
                    self.block.append(_line)

        return self.document
