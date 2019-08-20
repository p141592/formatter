from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class DB:
    """ Работа с базой
    Место с ручками sqlalchemy
    """
    __instance = None
    BASE = declarative_base()
    ENGINE = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/formatter')
    session = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.create_all()
            cls.session = cls.create_session()
            cls.__instance = super().__new__(cls)

        return cls.__instance

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

    def select(self):
        pass

    def insert(self, object):
        if not self.exists(object):
            self.session.add(object)
            self.session.commit()
