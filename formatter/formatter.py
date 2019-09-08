# Объект для преобразования базового дерева в дерево формата
import re

from formatter import Document


class BaseFormatRules:
    """Базовый класс правил формата"""
    def __init__(self, *args, **kwargs):
        self.RULES = dict()

    def get_backend(self, content):
        for _rule, backend in self.RULES.items():
            if re.match(_rule, content):
                return backend(content)

class RSTRules(BaseFormatRules):
    def __init__(self, *args, **kwargs):
        super(RSTRules, self).__init__(*args, **kwargs)
        self.RULES = {
            r"1": self.text_block
        }

    def text_block(content):
        pass


class Formatter:
    def __init__(self, format: BaseFormatRules):
        assert isinstance(format, BaseFormatRules), "Объект формата должен быть наследником BaseFormatRules"
        self.format = format

    def get_block_type(self, content):
        """Получение типа блока по ругулярному выражению"""
        pass

    def run(self, document):
        self.result = Document()
        for _block in document:
            self.format.get_backend(_block)
