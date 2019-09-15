import json

import pypandoc as pypandoc

from formatter.tree.nodes import Root


class Parser:
    """Деление документа на параграфы и блоки"""
    def __init__(self):
        """Принимает на вход объект Source и из него формирует Document"""
        self.root = Root()
        self.status = None

        self.document = None
        self.paragraph = None
        self.block = None
        self.line = None
        self.pandoc_types = set()

        self.prev_line = []  # Ссылка на 2 предидущих объекта
        self.position = 0
        self.line_number = 1

    def close_element(self):
        if self.block:
            self.block = None
            return
        if self.paragraph:
            self.paragraph = None
            return

    def append_element(self, index, content):
        if not self.paragraph:
            self.paragraph = self.document.create_child()

        if not self.block:
            self.block = self.paragraph.create_child()

        self.block.create_child(line_number=index, content=content)

    def read_document(self, file, format):
        try:
            _pandoc_json = pypandoc.convert_file(file, "json", format=format)
            pass

        except UnicodeDecodeError:
            print(f'Ошибка при чтении файла {self.document.path}')
            return

        return self.document

    def load(self, source):
        """Создание content_tree из документа

        1. format_file
        2. document -> pandoc -> JSON
        3. JSON -> content_tree
        """
        with source as _source:
            for _file in _source.files:
                self.document = self.root.create_child()
                self.read_document(_file, source.format)
        return self.root

    def parsing(self, tree, format):
        """Форматирование content_tree в файл формата

        1. content_tree -> JSON
        2. JSON -> pandoc -> format_file
        """
