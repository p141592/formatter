import os

from . import BaseTree

class Root(BaseTree):
    def __init__(self, *args, **kwargs):
        self.type = 'ROOT'
        self.children_type = Document
        super(Root, self).__init__(*args, **kwargs)

class Document(BaseTree):
    def __init__(self, file, *args, **kwargs):
        self.type = 'DOCUMENT'
        self.children_type = Block

        self.file = open(file)
        _, self.filename = os.path.split(file)
        self.path = file
        super(Document, self).__init__(*args, **kwargs)

class Block(BaseTree):
    def __init__(self, *args, **kwargs):
        self.type = 'BLOCK'
        self.children_type = Line
        super(Block, self).__init__(*args, **kwargs)

class Line(BaseTree):
    def __init__(self, *args, line_number=None, position=None, content=None, **kwargs):
        self.content = content # Готовое значение
        self.position = position # Позиция в списке children у родителя
        self.type = 'LINE' if content else 'BLANK'
        self.line_number = line_number
        self.format_sign = False
        super(Line, self).__init__(*args, **kwargs)

    def __bool__(self):
        return bool(self.content)
