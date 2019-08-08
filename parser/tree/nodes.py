import os

from parser.tree import BaseTree

class Root(BaseTree):
    def __init__(self):
        self.type = 'ROOT'
        super(Root, self).__init__()

class Document(BaseTree):
    def __init__(self, file):
        self.type = 'DOCUMENT'

        self.file = open(file)
        _, self.filename = os.path.split(file)
        self.path = file
        super(Document, self).__init__()

class Block(BaseTree):
    def __init__(self):
        self.type = 'BLOCK'
        super(Block, self).__init__()

class Line(BaseTree):
    def __init__(self, offset, source):
        self.type = 'LINE'
        self.offset = offset
        self.source = source # Содержит исходную строку целиком
        super(Line, self).__init__()

class Term(BaseTree):
    def __init__(self, content):
        self.type = 'TERM'
        super(Term, self).__init__(content = content)
