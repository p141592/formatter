import datetime
import uuid

from sqlalchemy import Column, TEXT, DateTime, ForeignKey, String, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from environs import Env

from parser.tree import BaseNode

env = Env()
env.read_env()

engine = create_engine(env.str('DB_URL', default='postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'))

Base = declarative_base(cls=BaseNode)

class DBRoot(Base):
    """
    Корень документации, по которому можно сделать выборку только по конкретным материалам
    """
    __tablename__ = "Root"

    url = Column(String, comment="")


class DBDocument(Base):
    """
    Хранение документа
    """
    __tablename__ = "Document"

    filename = Column(String(50), comment='Название документа')
    path = Column(String(100), comment='Путь до файла, который был объявлени при создании документа')

class DBNode(Base):
    """
    Таблица, для записи нод дерева
    """
    __tablename__ = "Node"

    type = Column(String(30))

    parent = Column(UUID, ForeignKey('node.id'))

    offset = Column(Integer, nullable=True) # Номер строки файла

    source = Column(TEXT, nullable=True)
    content = Column(TEXT, nullable=True)
    created_date = Column(DateTime, default=datetime.datetime.now)

    format_sign = Column(Boolean)
