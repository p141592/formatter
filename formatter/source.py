import os
import re
import time
from marshmallow import Schema, fields

from exceptions import SourceNotFoundException, PathException


class BaseSource:
    """Базовый объект
    - Контекст менеджер для работы с источниками
    - По переданной ссылке определяется, какой класс использовать для обработки исчтоника
    """
    REGEXP = None # регулярка для идентификации типа
    SEC_PATH = '/tmp/formatter' # Путь, куда можно сложить файлы

    class Serializer(Schema):
        url = fields.String()
        path = fields.String()

    @classmethod
    def init(cls, **kwargs):
        # Найти -- к какому объекту принадлежит URL
        data = cls.Serializer().load(kwargs)
        base_class = cls.get_source_class(**data)
        if not base_class:
            raise SourceNotFoundException

        # Передать аргументы в нужный подкласс
        # Вернуть объект
        return base_class(**data)

    @classmethod
    def get_source_class(cls, url, **kwargs):
        for _subclass in cls.__subclasses__():
            if _subclass.match_source_url(url):
                return _subclass

    @classmethod
    def match_source_url(cls, url):
        """Проверка URL на валидность"""
        return bool(re.match(cls.REGEXP, url))

    def match_files_regexp(self, filename):
        return bool(re.match(self.files_regexp, filename))

    @staticmethod
    def check_file(path):
        if os.path.exists(path):
            return path
        raise PathException

    @property
    def files(self):
        """Генератор, возвращающий дескриптор файла"""
        for root, dirs, files in os.walk(os.path.join(self.source_path, self.path)):
            for _file in files:
                if self.match_files_regexp(_file):
                    yield os.path.join(root, _file)

    def __init__(self, url, path, files_regexp):
        self.url = url
        self.path = path # Путь до файлов в исходнике
        self.files_regexp = files_regexp # Правило фильтрации файлов документации
        self.source_path = None # Куда мы положили новые файлы

    def fetch_files(self):
        raise NotImplementedError

    def remove_files(self):
        os.system(f'rm -f {self.source_path}')

    def __enter__(self):
        # Получить файлы из пути, распаковать в безопасную папку
        # Сохранить Путь до папки с файлами
        self.fetch_files()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Удалить файлы из папки
        return


class GitSource(BaseSource):
    REGEXP = r".*\.git$"

    def fetch_files(self):
        self.source_path = f'{self.SEC_PATH}/{time.time()}'
        os.system(f'git clone {self.source_path}')
