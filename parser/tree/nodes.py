import os

from . import BaseTree

class Root(BaseTree):
    def __init__(self, *args, **kwargs):
        super(Root, self).__init__(*args, **kwargs)
        self.children_type = Document

class Document(BaseTree):
    def __init__(self, file, *args, **kwargs):
        super(Document, self).__init__(file, *args, **kwargs)
        self.children_type = Block
        self.file = open(file)
        _, self.filename = os.path.split(file)
        self.path = file

class Block(BaseTree):
    def __init__(self, *args, **kwargs):
        super(Block, self).__init__(*args, **kwargs)
        self.children_type = Line

class Line(BaseTree):
    def __init__(self, *args, **kwargs):
        super(Line, self).__init__(*args, **kwargs)
        self.content = kwargs.get('content', None)  # Готовое значение
        self.line_number = kwargs.get('line_number', None)
        self.format_sign = False
