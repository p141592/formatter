import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from environs import Env

env = Env()
env.read_env()

engine = create_engine(env.str('DB_URL', default='postgresql+psycopg2://postgres:postgres@localhost:5432/postgres'))

Base = declarative_base()
