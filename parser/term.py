import hashlib

ALLOW_TYPES = (
    'LIST', 'BLOCK', 'ARTICLE', 'PARAGRAPH', 'HEAD', 'LINE', 'TERM', 'CODE',
)

BLOCK_TYPES = (
    'ARTICLE', 'HEAD', 'PARAGRAPH',
)

LINE_TYPES = (
    'CODE', 'TERM',
)


class Tree:
    ROOT = None

    def __init__(self, *args,
                 _type='term',
                 title=None,
                 offset=0,
                 parent=None,
                 content=None,
                 filename=None,
                 **kwargs
                 ):
        self.title = title
        self.children = []
        self.parent = parent
        self.hash = None
        self.__content = content
        self.offset = offset
        self.filename = filename
        self.type = _type

    def __str__(self):
        return f'__{self.type}__.content: {self.content}'

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

    @property
    def content(self):
        return self.__content or [str(_child) for _child in self.children]

    def get_line(self, number):
        if self.offset:
            return self

        for _child in self.children:
            result = _child.get_line(number)
            if result:
                return result

    def append(self, node):
        node.parent = self
        self.children.append(node)

    def set_type(self, _type):
        if _type in ALLOW_TYPES and self.type != _type:
            self.type = _type

    @staticmethod
    def get_line_sign(line):
        """
        Проверить строки на наличие признака строки
        :param line:
        :return: line, признак
        """
        if '*****' in line:
            return 'ARTICLE'
        elif '=====' in line:
            return 'PARAGRAPH'
        elif '-----' in line:
            return 'HEAD'
        elif line == '\n':
            return 'END'
        else:
            return 'LINE'

    @staticmethod
    def read(element, parent=None, offset=0):

        """
        Получает строку, разбирает ее
        Если встречает признак в строке -- Меняет тип для родителя

        Если сама строка является признаком -- Создается новый Block и возвращается
        :param offset: Номер строки
        :param parent: Родительский элемент дерева
        :param element: строка файла
        :return: parent елемент
        """

        if not parent:
            _node = Tree(_type='BLOCK')
            parent = _node
            Tree.ROOT = _node

        sign = Tree.get_line_sign(element)

        if sign == 'END':
            _node = Tree(_type='BLOCK')
            Tree.ROOT.append(_node)
            return _node

        if sign in BLOCK_TYPES:
            parent.set_type(sign)
            return parent

        line_element = Tree(_type='LINE', parent=parent)
        parent.append(line_element)

        for word in element.strip().split(' '):
            line_element.append(
                Tree(_type='TERM', content=word, parent=line_element, offset=offset)
            )
        print(Tree.ROOT)
        return parent


class CodeExcept(BaseException): pass


class TitleExcept(BaseException): pass


class TextExcept(BaseException): pass


class ListExcept(BaseException): pass


class BlockEndExcept(BaseException): pass


class HeadExcept(BaseException): pass


class ParagraphExcept(BaseException): pass


class FinishExcept(BaseException): pass
