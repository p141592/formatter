# Объект для преобразования базового дерева в дерево формата
import re

from formatter import Document
from formatter.exceptions import NotExceptedFormat
from formatter.tree.nodes import Code, Text, EmbedBlock, Phraze, Term, Link, Image, List, Column, Table

class BaseFormatRules:
    """Базовый класс правил формата

    Предоставляет базовые функции обработки формата
    Валидириует данные, перед добавлением в дерево
    """
    def __init__(self, *args, **kwargs):
        self.RULES = () # (r"regexp", node, backend)

    def get_backend(self, content):
        for rule, node, backend in self.RULES:
            if re.match(rule, content) and node.base_check(content):
                if backend:
                    return backend(content)
                return node(content)

        raise NotExceptedFormat(content)


class RSTRules(BaseFormatRules):
    def __init__(self, *args, **kwargs):
        super(RSTRules, self).__init__(*args, **kwargs)
        self.RULES = (
            (r"1", Text, None)
        )


class Formatter:
    def __init__(self, format: BaseFormatRules):
        assert isinstance(format, BaseFormatRules), "Объект формата должен быть наследником BaseFormatRules"
        self.format = format
        self.result = None

    def run(self, document):
        self.result = Document()
        for _block in document:
            self.format.get_backend(_block)
        return self.result
