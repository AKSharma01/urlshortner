from database.models import *
# from database.tables import UrlShortnerTable as us
class DB():
	
	def getByURL(self, model, value): 
		return get(model, value)

	def create(self, model, value):
		return store(model, value)

	def get(self, model, value= {}):
		return get(model, value)

	def filter(self, model, value={}):
		return filter(model, value)
