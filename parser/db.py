from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class DB:
    """ Работа с базой
    Место с ручками sqlalchemy
    """
    BASE = declarative_base()
    ENGINE = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')

    def __init__(self):
        self.session = self.create_session()

    def create_all(self):
        DB.BASE.metadata.create_all(DB.ENGINE)

    def create_session(self):
        _session = sessionmaker(bind=self.ENGINE)
        _session.configure(bind=self.ENGINE)
        return _session()

    def select(self):
        pass

    def insert(self, object):
        self.session.add(object)
        self.session.commit()
