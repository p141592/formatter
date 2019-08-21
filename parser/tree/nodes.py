import os

from . import BaseTree

class Root(BaseTree):
    def __init__(self, *args, **kwargs):
        super(Root, self).__init__(*args, **kwargs)
        self.children_type = Document

class Document(BaseTree):
    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.children_type = Block
        _file = kwargs.get('file')
        self.file = open(_file) if _file else None
        self.path, self.filename = os.path.split(kwargs.get('file')) if _file else (kwargs.get('path'), kwargs.get('filename'))

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

    def __bool__(self):
        return bool(self.content)
