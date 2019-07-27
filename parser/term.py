import hashlib
from collections import Iterable


class Term:
    """
    Базовый класс для объявление Term
    """
    offset = 0
    parent = None
    current = None
    root =

    def __new__(cls, iterator: Iterable[str]):
        """
        Разбирает строку, ищет признак
        Если встречается пуста строки
        Или признак отличается от пред идущего -> Создается Term и ему устанавликается родитель

        :param args:
        :param kwargs:
        :return:
        """
        for i in
        return TYPE_MAP[cls.get_sign(line)].__init__(
            offset=cls.offset, parent=cls.parent
        )
        return Code.__init__(*args, **kwargs)
        #return super(Term, cls).__new__(cls)

    def __init__(self, *args, **kwargs):
        self.offset = 0  # Номер строки в статье
        self.child = []
        self.parent = None
        self.content = []
        self.hash = None

    def get_sign(self, line):
        if line == '\n':
            return None
        elif '=' in line:
            return 'title'
        elif '*' in line:
            return ''

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


TYPE_MAP = {
    '    ': Code,

}
