import os
import uuid

from tree.mixins import TreeLenMixin
from tree import BaseTree
from parser import ALLOW_TYPES


class Tree(BaseTree):
    pass


class Root(Tree):
    def __init__(self):
        self.type = 'ROOT'
        super(Root, self).__init__()

    def __str__(self):
        result = [
            f'{self.type}:{self.id}: {hash(self)}',
            f'LENGTH: \n'
            f'  DOCUMENTS: {self.documents_length()}\n'
            f'  BLOCKS: {self.blocks_length()}\n'
            f'  LINES: {self.line_length()}\n'
            f'  TERMS: {len(self)}\n'
            f'  SYMBOLS: {self.symbol_length()}'
        ]

        return "\n".join(result)

class Document(Tree):
    def __init__(self, file):
        self.type = 'DOCUMENT'
        assert Document.check_file(file), "Файл документа не существует"

        self.file = open(file)
        _, self.filename = os.path.split(file)
        self.path = file
        super(Document, self).__init__()

    def __str__(self):
        return self.filename

    @staticmethod
    def check_file(document):
        return os.path.exists(document)

class Block(Tree):
    def __init__(self):
        self.type = 'BLOCK'
        super(Block, self).__init__()

class Line(Tree):
    def __init__(self, offset):
        self.type = 'LINE'
        self.offset = offset
        super(Line, self).__init__()

class Term(Tree):
    def __init__(self, content):
        self.type = 'TERM'
        super(Term, self).__init__(content = content)
