import os

from formatter.tree import BaseTree


class Root(BaseTree):
    def __init__(self, *args, **kwargs):
        super(Root, self).__init__(*args, **kwargs)
        self.children_type = Document


class Document(BaseTree):
    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.children_type = Paragraph
        _file = kwargs.get('file')
        self.file = open(_file) if _file else None
        self.path, self.filename = os.path.split(kwargs.get('file')) if _file else (
        kwargs.get('path'), kwargs.get('filename'))

    def __str__(self):
        return self.filename


class Paragraph(BaseTree):
    """Разделение по 2 пустые строки"""
    def __init__(self, *args, **kwargs):
        super(Paragraph, self).__init__(*args, **kwargs)
        self.children_type = Block


class Block(BaseTree):
    """Разделение пустой строкой"""
    def __init__(self, *args, **kwargs):
        super(Block, self).__init__(*args, **kwargs)
        self.children_type = Line


class Line(BaseTree):
    def __init__(self, *args, **kwargs):
        super(Line, self).__init__(*args, **kwargs)
        self.content = kwargs.get('content', None)  # Готовое значение
        self.line_number = kwargs.get('line_number', None)

    def __bool__(self):
        return bool(self.content)

# Базовые элементы форматированного дерева


class Sentence(BaseTree):
    def __init__(self, *args, **kwargs):
        super(Sentence, self).__init__(*args, **kwargs)


class Text(Block):
    """Текстовый блок"""
    def __init__(self, *args, **kwargs):
        super(Text, self).__init__(*args, **kwargs)
        self.children_type = Sentence


class Code(Block):
    """Блок с кодом"""
    def __init__(self, *args, **kwargs):
        super(Code, self).__init__(*args, **kwargs)
        self.children_type = Line


class EmbedBlock(Block):
    """Embed элемент с интерактивом"""
    def __init__(self, *args, **kwargs):
        super(EmbedBlock, self).__init__(*args, **kwargs)
        self.children_type = Line


class Table(Block):
    """Таблица"""
    def __init__(self, *args, **kwargs):
        super(Table, self).__init__(*args, **kwargs)
        self.children_type = Column


class Column(BaseTree):
    """Колонка"""
    def __init__(self, *args, **kwargs):
        super(Column, self).__init__(*args, **kwargs)
        self.children_type = None


class List(BaseTree):
    """Список"""
    def __init__(self, *args, **kwargs):
        super(List, self).__init__(*args, **kwargs)
        self.children_type = List


class Image(BaseTree):
    """Хранение изображения"""
    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
        self.children_type = None


class Link(BaseTree):
    """Хранение ссылки"""
    def __init__(self, *args, **kwargs):
        super(Link, self).__init__(*args, **kwargs)
        self.children_type = None

# Атомарные объекты дерева
# Эти элементы должны храниться в content


class Term(BaseTree):
    """Слово"""
    def __init__(self, *args, **kwargs):
        super(Term, self).__init__(*args, **kwargs)
        self.children_type = None


class Phraze(BaseTree):
    """Не делимые выражения"""
    def __init__(self, *args, **kwargs):
        super(Phraze, self).__init__(*args, **kwargs)
        self.children_type = Term
