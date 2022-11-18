
# defines the database tables and data constrainst. 
# initalizes tables to exist so data can be accepted from API.

from datetime import datetime
from sqlalchemy import (
	Table, 
	Column, 
	Numeric, 
	DateTime, 
	String, 
	Integer, 
	ForeignKey, 
	func
)
from engine.db_con import *




class Vault1_Model(Base):
	__tablename__ = "Vault1"
	id = Column(Integer, primary_key=True)
	name = Column(String(255), nullable=False)
	website = Column(String(255), nullable=False)
	password = Column(String(255), nullable=False)
	created_on = Column(DateTime(), default=datetime.now, nullable=False)
	updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False)

	def __repr__(self):
		return "<Vault1(id={self.id!r}, name={self.name!r}, website={self.website!r}, password={self.password!r}, created_on={self.created_on!r}, created_on{self.updated_on!r})>".format(self=self)



class Vault2_Model(Base):
	__tablename__ = "Vault2"
	id = Column(Integer, primary_key=True)
	name = Column(String(255), nullable=False)
	website = Column(String(255), nullable=False)
	password = Column(String(255), nullable=False)
	created_on = Column(DateTime(), default=datetime.now, nullable=False)
	updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False)

	def __repr__(self):
		return "<Vault1(id={self.id!r}, name={self.name!r}, website={self.website!r}, password={self.password!r}, created_on={self.created_on!r}, created_on{self.updated_on!r})>".format(self=self)




Vault1_Model()
Vault2_Model()

Base.metadata.create_all(db_engine)




