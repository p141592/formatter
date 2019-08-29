class BaseSource:
    """Базовый объект
    - Контекст менеджер для работы с источниками
    - По переданной ссылке определяется, какой класс использовать для обработки исчтоника
    """
    PARSER = None

    def __init__(self, url, *args, **kwargs):
        pass

    def get_source_class(self, url):
        pass


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
