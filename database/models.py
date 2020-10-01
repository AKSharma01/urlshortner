# from All import *
from setting import ENVSetting
import importlib
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy import create_engine


session = session.Session(bind=create_engine(ENVSetting().createConnetionLink()))


def store(modelName, values):
	module = importlib.import_module('database.tables.'+modelName+'Table')
	modelName = getattr(module, modelName)
	print values
	md = modelName(**values)
	session.add(md)
	session.commit()


def get(modelName, values={}):
	# print modelName
	module = importlib.import_module('database.tables.'+modelName+'Table')
	modelName = getattr(module, modelName)
	data = modelName.query.get(**values)
	transformedFilterData = []
	for i in data:
		transformedFilterData.append(i.transform())
	return transformedFilterData


def filter(modelName, values):
	module = importlib.import_module('database.tables.'+modelName+'Table')
	modelName = getattr(module, modelName)
	filterData = modelName.query.filter_by(**values).all()
	transformedFilterData = []
	for i in filterData:
		transformedFilterData.append(i.transform())
	return transformedFilterData

def delete(modelName, values):
	pass

def upgrade(modelName, values, newValue):
	module = importlib.import_module('database.tables.'+modelName+'Table')
	modelName = getattr(module, modelName)
	filterData = modelName.query.filter_by(no_of_hits=values).update(**values)
	session.commit()
