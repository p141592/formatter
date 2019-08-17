import os

from parser.db import DB
from parser.tree.models import DBLine, DBTerm, DBRoot, DBDocument, DBBlock
from . import BaseTree

class Root(BaseTree):
    DB_MODEL = DBRoot

    def __init__(self):
        self.type = 'ROOT'
        self.db = DB()
        self.children_type = Document
        super(Root, self).__init__()

class Document(BaseTree):
    DB_MODEL = DBDocument

    def __init__(self, file):
        self.type = 'DOCUMENT'
        self.children_type = Block
        self.file = open(file)
        _, self.filename = os.path.split(file)
        self.path = file
        super(Document, self).__init__()

class Block(BaseTree):
    DB_MODEL = DBBlock

    def __init__(self):
        self.type = 'BLOCK'
        self.children_type = Line
        super(Block, self).__init__()

class Line(BaseTree):
    DB_MODEL = DBLine

    def __init__(self, offset, source=None):
        self.type = 'LINE' if source else 'BLANK'
        self.offset = offset
        self.source = source # Содержит исходную строку целиком
        self.format_sign = False
        super(Line, self).__init__()

class Sentence(BaseTree):
    def __init__(self):
        self.type = 'SENTENCE'
        self.children_type = Term
        super(Sentence, self).__init__()


class Term(BaseTree):
    DB_MODEL = DBTerm

    def __init__(self, content):
        self.type = 'TERM'
        self.content = content # Обработанный контент
        super(Term, self).__init__()
