import os

from parser.term import Document, Line, Term, Root, BLOCK_TYPES, Block
from parser.utils.tools import printProgressBar


class Parser:
    """
    Преобразование файла в объект Document
    """
    FILES_LENGTH = 0

    def __init__(self):
        self.root = Root()
        self.document = None
        self.line = None
        self.block = None
        self.offset = 1
        self.files = []

    @staticmethod
    def get_line_sign(line):
        """
        Проверить строки на наличие признака строки
        :param line:
        :return: line, признак
        """
        if '*****' in line:
            return 'ARTICLE'
        elif '=====' in line:
            return 'PARAGRAPH'
        elif '-----' in line:
            return 'HEAD'
        elif line == '\n':
            return 'END'

    def read_word(self, word):
        return Term(content=word)

    def block_magic(func):
        def magic(self, line, *args, **kwargs):
            if line and not self.block:
                self.block = Block()
                self.document.append(self.block)

            sign = self.get_line_sign(line)
            if sign in BLOCK_TYPES:
                self.block.set_type(sign)

                if sign == 'END':
                    self.block = None
                return None

            return func(self, line, *args, **kwargs)
        return magic

    @block_magic
    def read_line(self, line):
        self.line = Line(offset=self.offset)

        for _word in line.strip().split(' '):
            self.line.append(self.read_word(_word))

        self.offset += 1
        return self.line

    def read_document(self, document):
        self.document = Document(document)
        with self.document.file as f:
            for line in f.readlines():
                _line = self.read_line(line)
                if _line:
                    self.block.append(_line)


        return self.document

    def read_all_source(self, dir):
        for root, dirs, files in os.walk(dir):
            for _file in files:
                self.files.append(os.path.join(root, _file))

        self.FILES_LENGTH = len(self.files)

        print(f'DOCUMENTS IN QUEUE: {self.FILES_LENGTH}')

        items = list(self.files)
        l = len(items)

        printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
        for i, item in enumerate(items):
            _document = self.read_document(self.files.pop())
            if _document:
                self.root.append(_document)

            printProgressBar(i + 1, l, prefix='Progress:', suffix='Complete', length=50)


        return self.root
