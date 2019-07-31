import os
import uuid


ALLOW_TYPES = (
    'LIST', 'BLOCK', 'ARTICLE', 'PARAGRAPH', 'HEAD', 'LINE', 'TERM', 'CODE', 'DOCUMENT'
)

BLOCK_TYPES = (
    'ARTICLE', 'HEAD', 'PARAGRAPH', 'CODE', 'END'
)


class Tree:
    def __init__(self, *args,
                 parent=None,
                 content=None,
                 **kwargs
                 ):
        self.id = uuid.uuid4()
        self.children = []
        self.parent = parent
        self.hash = None
        self.content = content

    def __str__(self):
        result = [f'HEAD: {self.type}:{self.id}: {hash(self)}']
        if self.content:
            result.append(f'CONTENT: {self.content}\n')
        if self.children:
            result.append(f'CHILDREN_LENGTH: {len(self.children)}')

        return "\n".join(result)


    def __len__(self):
        """
        Обходит дерево, считает количество термов
        :return: Количество Term элементов
        """
        _result = 0
        for i in self.children:
            _result += len(i) if i.children else 1
        return _result

    def get_parent(self, parent_type):
        assert parent_type in ALLOW_TYPES, f"Указанный тип родителя \"{parent_type}\" запрещен"
        if self.type == parent_type:
            return self

        if self.parent:
            return self.parent.get_parent(parent_type)
        print(self)

    def symbol_length(self):
        if self.content:
            return len(self.content)
        _result = 0
        for _child in self.children:
            _result += _child.symbol_length()
        return _result

    def documents_length(self):
        if self.type == 'DOCUMENT':
            return 1

        _result = 0
        for _child in self.children:
            _result += _child.documents_length()
        return _result

    def blocks_length(self):
        if self.type in BLOCK_TYPES:
            return 1

        _result = 0
        for _child in self.children:
            _result += _child.blocks_length()
        return _result

    def search(self, term):
        if self.content and self.content == term:
            print(f'{self.get_parent("DOCUMENT").filename}: {self.get_parent("LINE").offset}')

        for _child in self.children:
            _child.search(term)

    def line_length(self):
        if self.type == 'LINE':
            return 1

        _result = 0
        for _child in self.children:
            _result += _child.line_length()
        return _result

    def set_type(self, type):
        if type in ALLOW_TYPES and self.type != type:
            self.type = type


    def get_line(self, number):
        if self.offset:
            return self

        for _child in self.children:
            result = _child.get_line(number)
            if result:
                return result

    def append(self, node):
        node.parent = self
        self.hash = None
        self.children.append(node)


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
