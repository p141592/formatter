import hashlib
import os


class Term:
    """
    Базовый класс для объявление Term
    """
    def __init__(self, line):
        self.offset = 0  # Номер строки в статье
        self.content = []
        self.hash = None

    def __len__(self):
        return len(self.content)

    def __hash__(self):
        if not self.hash:
            assert self.content, "Объект пуст"
            self.hash = hashlib.md5(
                (
                        str(self.offset) + "".join(self.content)
                ).encode('utf-8')
            ).hexdigest()

        return self.hash


class Code(Term):
    """
    Определяет блок кода
    """


class Title(Term):
    """
    Объект заголовка
    """


class Text(Term):
    """
    Объект текста
    """


class List(Term):
    """
    Элементы списка
    """


class Article:
    """
    Объект, оборачивающий контент
    """
    def __init__(self):
        self.children = []
        self.hash = None

    def __hash__(self) -> str:
        """
        Конкатинация хешей детей
        :return:  hexdigest:srt
        """
        if not self.hash:
            assert self.children, "Объект статьи пуст"
            _children_hash = []
            for _term in self.children:
                assert issubclass(Term, _term), "Article содержит не допустимый тип объекта"
                _children_hash.append(hash(_term))

            self.hash = hashlib.md5(
                "".join(_children_hash).encode('utf-8')
            ).hexdigest()
        return self.hash


class Parser:
    """
    Преобразование файла в объект Article
    """
    def __init__(self, document):
        self.file = None
        self.text = None
        self.content = Article()

        self.check_document(document)

    def check_document(self, document):
        if os.path.exists(document):
            self.file = document
        elif isinstance(document, str):
            self.text = document
        else:
            assert "Не поддерживаемый тип документа"

    def parse(self, line):
        pass

    def start(self):
        with open(self.file) as f:
            self.parse(f.readline())
        return


if __name__ == '__main__':
    assert Parser("Тест").start() == Article([Text("Тест")])
