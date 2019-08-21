from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class DB:
    """ Работа с базой
    Место с ручками sqlalchemy
    """
    __instance = None
    BASE = declarative_base()
    ENGINE = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/formatter', pool_size=50, max_overflow=20)
    METADATA = MetaData()
    session = None

    def __init__(self):
        self.create_all()
        self.session = self.create_session()

    @staticmethod
    def create_all():
        DB.BASE.metadata.create_all(DB.ENGINE)

    @classmethod
    def create_session(cls):
        _session = sessionmaker(bind=cls.ENGINE)
        _session.configure(bind=cls.ENGINE)
        return _session()

    def exists(self, object):
        """Проверка объекта на существование"""
        instance = self.session.query(object.__class__).filter_by(id=object.id).first()
        return bool(instance)

    def close(self):
        self.session.close()

    def add(self, object):
        if not self.exists(object):
            self.session.add(object)

    def commit(self, generator=None):
        """Выполнить коммит объектов"""
        if generator:
            self.session.add_all(iter(generator))
        self.session.commit()
