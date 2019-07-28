import os

from parser.term import Term, TitleExcept, Title, CodeExcept, Code, HeadExcept, ParagraphExcept, ListExcept


class Parser:
    """
    Преобразование файла в объект Article
    """
    def __init__(self, document):
        self.content = self.check_document(document)
        self.root = None
        self.terms = None
        self.offset = 0

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

    @staticmethod
    def check_line(line):
        if '===' in line:
            raise TitleExcept
        if '***' in line:
            raise HeadExcept
        if '---' in line:
            raise ParagraphExcept
        if line[:3] == '    ':
            raise CodeExcept
        if line[0] == '*':
            raise ListExcept

    @staticmethod
    def read_line(line):
        try:
            Parser.check_line(line)
        except TitleExcept:
            return Title(line)
        except CodeExcept:
            return Code()

    @staticmethod
    def read_element(word):
        for element in word:
            pass

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
        print(_term)
        _term.read_line(_term)
