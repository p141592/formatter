import hashlib


class Term:
    """
    Базовый класс для объявление Term
    """
    offset = 0
    parent = None
    current = None
    root = None

    def __init__(self, *args, **kwargs):
        self.offset = 0  # Номер строки в статье
        self.child = []
        self.parent = None
        self.content = []
        self.hash = None

    def append(self, line):
        self.content.append(line)

    def __len__(self):
        return len(self.content)

    def __hash__(self):
        assert self.content, "Объект пуст"

        if not self.hash:
            _key = str(self.offset) + "".join(self.content)
            _result = hashlib.md5(_key.encode('utf-8')).hexdigest()
            self.hash = int(_result, 16)

        return self.hash


class Code(Term):
    """
    Определяет блок кода
    """


class CodeExcept(BaseException): pass


class Title(Term):
    """
    Объект заголовка
    """


class TitleExcept(BaseException): pass


class Text(Term):
    """
    Объект текста
    """


class TextExcept(BaseException): pass


class List(Term):
    """
    Элементы списка
    """


class ListExcept(BaseException): pass


class BlockEndExcept(BaseException): pass


class HeadExcept(BaseException): pass


class ParagraphExcept(BaseException): pass


class FinishExcept(BaseException): pass
