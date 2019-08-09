import os

from sqlalchemy import Column, Integer, TEXT, Boolean, String

from parser.tree import BaseTree

class Root(BaseTree):
    __tablename__ = 'Root'

    def __init__(self):
        self.type = 'ROOT'
        super(Root, self).__init__()

class Document(BaseTree):
    __tablename__ = 'Document'

    filename = Column(String(50), comment='Название документа')
    path = Column(String(100), comment='Путь до файла, который был объявлени при создании документа')

    def __init__(self, file):
        self.type = 'DOCUMENT'

        self.file = open(file)
        _, self.filename = os.path.split(file)
        self.path = file
        super(Document, self).__init__()

class Block(BaseTree):
    __tablename__ = 'Block'

    def __init__(self):
        self.type = 'BLOCK'
        super(Block, self).__init__()

class Line(BaseTree):
    __tablename__ = 'Line'

    offset = Column(Integer)
    source = Column(TEXT)
    format_sign = Column(Boolean)

    def __init__(self, offset, source=None):
        self.type = 'LINE'
        self.offset = offset
        self.source = source # Содержит исходную строку целиком
        self.format_sign = False
        super(Line, self).__init__()

class BlankLine(Line):
    __tablename__ = 'BlankLine'

    def __init__(self, *args, **kwargs):
        self.type = 'BLANK'
        super(BlankLine, self).__init__(*args, **kwargs)

class RawLine(Line):
    __tablename__ = 'RawLine'

    def __init__(self, *args, **kwargs):
        self.type = 'RAW'
        super(RawLine, self).__init__(*args, **kwargs)

class Term(BaseTree):
    __tablename__ = 'Term'

    def __init__(self, content):
        self.type = 'TERM'
        super(Term, self).__init__(content = content)
