import hashlib

TYPES = (

)


class Tree:
    def __init__(self, *args, **kwargs):
        self.title = None
        self.children = []
        self.parent = None
        self.hash = None
        self.content = None
        self.offset = 0
        self.filename = None
        self.type = None

    def __hash__(self):
        assert self.content, "Объект пуст"

        if not self.hash:
            _hash = None
            if not self.children:
                _hash = str(self.offset) + self.content
            else:
                _hash = "".join((hash(child) for child in self.children))

            self.hash = int(hashlib.md5(_hash.encode('utf-8')).hexdigest(), 16)

        return self.hash

    def __len__(self):
        """
        Обходит дерево, считает количество термов
        :return: Количество Term элементов
        """
        _result = 0
        for i in self.children:
            _result += len(i) if i.children else 1
        return _result

    def get_line(self, number):
        if self.offset:
            return self

        for _child in self.children:
            result = _child.get_line(number)
            if result:
                return result

    @staticmethod
    def read(element, parent=None):
        """
        Собирает
        :param parent: Родительский элемент дерева
        :param element: строка файла
        :return: parent елемент
        """


class CodeExcept(BaseException): pass


class TitleExcept(BaseException): pass


class TextExcept(BaseException): pass


class ListExcept(BaseException): pass


class BlockEndExcept(BaseException): pass


class HeadExcept(BaseException): pass


class ParagraphExcept(BaseException): pass


class FinishExcept(BaseException): pass
