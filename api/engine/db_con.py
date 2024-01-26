
# configures connects and builds inital database to accept API data

import sqlalchemy as sqla
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from dotenv import *
from os import getenv


config = find_dotenv("config.env")

DRIVER = get_key(config,'DRIVER')
USERNAME = get_key(config,'USERNAME')
PASSWORD = get_key(config,'PASSWORD')
HOST = get_key(config,'HOST')
PORT = get_key(config,'PORT')
DB_NAME = get_key(config, 'DB_NAME')
DEBUG = get_key(config, 'DEBUG')


Base = declarative_base()


# from os get operating system. if linux change forward slashs to back slashs
if DEBUG == "True":
	# IF DEBUG == True: DB_NAME = 'vault1_TEST' else: DB_NAME = 'vault1_prod'
	db_engine = sqla.create_engine('{}://{}:{}@{}:{}/'.format(DRIVER,USERNAME,PASSWORD,HOST,PORT))

	connection = db_engine.connect()

	with connection as conn:
		conn.execute(f"DROP DATABASE IF EXISTS {DB_NAME}")
		conn.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
		conn.execute(f"use {DB_NAME}")

else:
	db_engine = sqla.create_engine('{}://{}:{}@{}:{}/{}'.format(DRIVER,USERNAME,PASSWORD,HOST,PORT,DB_NAME))
	connection = db_engine.connect()
	connection.execute(f"use {DB_NAME}")


# used for resources to commit API requests to DB.
Session = scoped_session(sessionmaker(bind = db_engine))
session = Session()



# used with middleware and DB connection initialization handling.
session_factory = sessionmaker(bind=db_engine)
Session = scoped_session(session_factory)



db_engine.connect()
Base.metadata.create_all(db_engine)

