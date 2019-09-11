import re

from formatter import NotExceptedFormat


class BaseFormatRules:
    """Базовый класс правил формата

    Предоставляет базовые функции обработки формата
    Валидириует данные, перед добавлением в дерево
    """
    def __init__(self, *args, **kwargs):
        self.DEFAULT_BACKEND = None # Используется, если в backend нужно загрузить следующие n блоков
        self.RULES = () # (r"regexp", node, backend)

    def get_backend(self, content):
        # Закрытие / открытие блока
        # В некоторых случаях нужно собрать контект следующих блоков, пока не будет признака завершения

        if self.DEFAULT_BACKEND:
            return self.DEFAULT_BACKEND(content)

        for rule, node, backend in self.RULES:
            if re.match(rule, content) and node.base_check(content):
                if backend:
                    return backend(content)
                return node(content)

        raise NotExceptedFormat(content)
