class BaseSource:
    """Базовый объект
    - Контекст менеджер для работы с источниками
    - Генератор, которы вызывается Parser-ом и создает дерево
    - Ссылку на конструктор класса Parser, подходящий к этому типу источника
    """
    PARSER = None

    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class GitSource(BaseSource):
    def __init__(self, url):
        super(GitSource, self).__init__()


class FileSource(BaseSource):
    def __init__(self):
        super(FileSource, self).__init__()


class DBSource(BaseSource):
    def __init__(self):
        super(DBSource, self).__init__()


class UrlSource(BaseSource):
    def __init__(self):
        super(UrlSource, self).__init__()
