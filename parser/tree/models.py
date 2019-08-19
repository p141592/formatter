import datetime
import uuid

from sqlalchemy import Column, TEXT, DateTime, ForeignKey, String, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID

from parser.db import DB

class DBRoot(DB.BASE):
    __tablename__ = "Root"

    id = Column(UUID, default=uuid.uuid1, primary_key=True)
    url = Column(String, comment="")
    created_date = Column(DateTime, default=datetime.datetime.now)

class DBDocument(DB.BASE):
    __tablename__ = "Document"

    id = Column(UUID, default=uuid.uuid1, primary_key=True)
    parent = Column(UUID, ForeignKey('Root.id'))
    created_date = Column(DateTime, default=datetime.datetime.now)
    filename = Column(String(50), comment='Название документа')
    path = Column(String(100), comment='Путь до файла, который был объявлени при создании документа')

class DBBlock(DB.BASE):
    __tablename__ = "Block"

    id = Column(UUID, default=uuid.uuid1, primary_key=True)
    parent = Column(UUID, ForeignKey('Document.id'))
    created_date = Column(DateTime, default=datetime.datetime.now)

class DBLine(DB.BASE):
    __tablename__ = "Line"

    id = Column(UUID, default=uuid.uuid1, primary_key=True)
    parent = Column(UUID, ForeignKey('Block.id'))
    created_date = Column(DateTime, default=datetime.datetime.now)
    type = Column(String(30))
    content = Column(TEXT, nullable=True)
    line_number = Column(Integer, nullable=True)
    format_sign = Column(Boolean)
