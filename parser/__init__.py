import os

from parser.term import Term


class Parser:
    """
    Преобразование файла в объект Article
    """
    def __init__(self, document):
        self.content = self.check_document(document)
        self.title = None
        self.terms = None

    @staticmethod
    def check_document(document):
        if os.path.exists(document):
            return document
        raise TypeError

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    # Парсинг контента
    # Запись контента в базу
    # Сериализация
    # Десериализация
    def start(self):
        with open(self.content) as f:
            Term(f)
        return self


def start(document):
    with Parser(document) as _term:
        _term.start()
