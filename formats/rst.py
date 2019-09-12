from formatter import BaseFormatRules
from formatter.tree.nodes import Text


class RSTRules(BaseFormatRules):
    def __init__(self, *args, **kwargs):
        super(RSTRules, self).__init__(*args, **kwargs)
        self.LINE_RULES = (
            (r"^=+$|^-+$|^~+$|^\"+$", None, self.title),
            (r"\*{2}.*\*{2}", None, self.bold),
            (r"", None, self.italic), # TODO: Текст курсивом
            (r"\`{2}.*\`{2}", None, self.pre), # Текст как есть
        )

        self.BLOCK_RULES = (
            #
            (r"1", Text, None),
            #
            (r"", None, self.table),
            #
            (r"(^\s{0,})(\*|\-|\#\.|\d\.)(\s)(.*)", None, self.list),
            #
            (r"", None, self.definition),
            #
            (r"", None, self.epigraph),
            #
            (r"", None, self.footnote),
            #
            (r"", None, self.code),
            #
            (r"", None, self.link),
            #
            (r"", None, self.line),
            #
            (r"", None, self.image),
            #
            (r"", None, self.hint),

        )

    # backend
        # На этом моменте я должен получить контент, который содержит контент этого блока
        # и преобразовать его в элементы дерева

    def table(self, content):
        pass

    def list(self, content):
        pass

    def definition(self, content):
        pass

    def epigraph(self, content):
        pass

    def footnote(self, content):
        pass

    def code(self, content):
        pass

    def link(self, content):
        pass

    def line(self, content):
        pass

    def image(self, content):
        pass

    def hint(self, content):
        pass
