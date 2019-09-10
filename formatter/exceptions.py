class PathException(Exception):
    """Вызывается, если файл документа не существует"""


class SourceNotFoundException(Exception):
    """Не найден класс для обработки указанного URL"""


class SourceUrlConnectFailed(Exception):
    """URL не доступен"""


class NotExceptedFormat(Exception):
    def __init__(self, content):
        self.content = content
        self.message = "Правило для объекта не найдено"


class ContentValueException(Exception):
    def __init__(self, content):
        self.content = content
        self.message = "Данные контена не валидны для добавления в дерево"


class ArgumentsException(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.message = "В конструктор ноды передан не верный набор аргументов"