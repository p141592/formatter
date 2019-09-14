import re

from formats import BaseFormatRules
from formatter.exceptions import NotExceptedFormat
from formatter.source import BaseSource
from formatter.parser import Parser
from formatter.tree import BaseTree
from formatter.tree.nodes import Root, Document, Paragraph, Block, Line


class Formatter:
    """Получение фалай формата, получение AST дерева, преобразование в собственное дерево"""
    def __init__(self, format: BaseFormatRules):
        assert isinstance(format, BaseFormatRules), "Объект формата должен быть наследником BaseFormatRules"
        self.format = format
        self.result = None

    def run(self, document):
        self.result = Document()
        for _block in document:
            self.format.get_backend(_block)
        return self.result


__package_name__ = 'stformatter'
__version__ = '0.2.2'
__author__ = 'Baryshnikov Nikolay'
__author_email__ = 'mr.boiled@gmail.com'
__description__ = '''A Python formatter from formats like rst and markdown to the content tree'''
__url__ = 'https://github.com/p141592/stformatter'

__all__ = (
    'BaseSource',
    'Parser',
    'BaseTree',
    'Root',
    'Document',
    'Paragraph',
    'Block',
    'Line'
)
