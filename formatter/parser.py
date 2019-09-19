import json

import pypandoc as pypandoc


class Parser:
    """Сбор слов для перевода"""
    def __init__(self):
        """Принимает на вход объект Source и из него формирует Document"""
        self.document = None

    def from_dict(self, block):
        t, c = block.items()
        return

    def read_document(self, file, format):
        # Чтение документа
        try:
            for block in json.loads(pypandoc.convert_file(file, "json", format=format)).get('blocks'):
                self.document._append(self.from_dict(block))

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
