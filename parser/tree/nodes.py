import os

from parser.tree.models import DBLine, DBTerm, DBRoot, DBDocument, DBBlock
from . import BaseTree

class Root(BaseTree):
    DB_MODEL = DBRoot

    def __init__(self):
        self.type = 'ROOT'
        super(Root, self).__init__()

class Document(BaseTree):
    DB_MODEL = DBDocument

    def __init__(self, file):
        self.type = 'DOCUMENT'

        self.file = open(file)
        _, self.filename = os.path.split(file)
        self.path = file
        super(Document, self).__init__()

class Block(BaseTree):
    DB_MODEL = DBBlock

    def __init__(self):
        self.type = 'BLOCK'
        super(Block, self).__init__()

class Line(BaseTree):
    DB_MODEL = DBLine

    def __init__(self, offset, source=None):
        self.type = 'LINE'
        self.offset = offset
        self.source = source # Содержит исходную строку целиком
        self.format_sign = False
        super(Line, self).__init__()

class BlankLine(Line):
    def __init__(self, *args, **kwargs):
        self.type = 'BLANK'
        super(BlankLine, self).__init__(*args, **kwargs)

class RawLine(Line):
    def __init__(self, *args, **kwargs):
        self.type = 'RAW'
        super(RawLine, self).__init__(*args, **kwargs)

class Term(BaseTree):
    DB_MODEL = DBTerm

    def __init__(self, content):
        self.type = 'TERM'
        self.content = content # Обработанный контент
        super(Term, self).__init__()
