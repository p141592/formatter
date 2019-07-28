import os

from parser.term import Tree


class Parser:
    """
    Преобразование файла в объект Article
    """

    def __init__(self, document):
        self.content = self.check_document(document)
        self.root = None
        self.terms = None
        self.offset = 1

    @staticmethod
    def check_document(document):
        if os.path.exists(document):
            return document
        raise TypeError

    def __enter__(self):
        self.content = open(self.content)
        return self.content.readlines()

    def __exit__(self, *exc):
        return self.content.close()

    # Парсинг контента
    # Запись контента в базу
    # Сериализация
    # Десериализация
    def start(self):
        parent = None
        with open(self.content) as f:
            for line in f.readlines():
                parent = Tree.read(line, parent)
                Tree(offset=self.offset)
                self.offset += 1
        return self
