from parser import BLOCK_TYPES


class TreeLenMixin:
    def symbol_length(self):
        if self.content:
            return len(self.content)
        _result = 0
        for _child in self.children:
            _result += _child.symbol_length()
        return _result

    def documents_length(self):
        if self.type == 'DOCUMENT':
            return 1

        _result = 0
        for _child in self.children:
            _result += _child.documents_length()
        return _result

    def blocks_length(self):
        if self.type in BLOCK_TYPES:
            return 1

        _result = 0
        for _child in self.children:
            _result += _child.blocks_length()
        return _result

    def line_length(self):
        if self.type == 'LINE':
            return 1

        _result = 0
        for _child in self.children:
            _result += _child.line_length()
        return _result

    def __len__(self):
        """
        Обходит дерево, считает количество термов
        :return: Количество Term элементов
        """
        _result = 0
        for i in self.children:
            _result += len(i) if i.children else 1
        return _result
