# from database.tables.UrlShortnerTable import UrlShortner
from se.urlShortner.models import DB
from random import choice
from flask import jsonify
import uuid


class urlShorten:
	def __init__(self):
		self.dbOpration = DB()

	def shorturl(self, url):
		check = self.dbOpration.filter('UrlShortner', {
			'original_url' : url
		})
		try:
			if check == []:
				myHash = self.hashGenerator()
				while(self.dbOpration.filter('UrlShortner', {'short_url':myHash})!=[]):
					myHash = self.hashGenerator()
				shurl = {
					'id' : self.generateUniqueCode(),
					'original_url' : url,
					'short_url' : myHash
				}
				self.dbOpration.create('UrlShortner', shurl)
				return myHash
				# return myHash, 200, None
			else : 
				return check[0]
		except Exception as e: 
			raise e

	def visit(self, shortnerId):
		from database.models import *
		print self.dbOpration.filter('UrlShortner' , {
					'short_url' : shortnerId	
				})[0]['noOfHits'] +1
		upgrade('UrlShortner', shortnerId, {
				'no_of_hits' : self.dbOpration.filter('UrlShortner' , {
					'short_url' : shortnerId	
				})[0]['noOfHits'] +1
			})
		pass


	def generateUrl(self):
		return self.hashGenerator()
		# return 'https://se.io/'+self.mygenrator()

	def hashGenerator(self):
		ch = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321' 
		myval = []
		for i in range(10):
			myval.append(choice(ch))
		return ''.join(myval)

	def myUrlList(self):
		return self.dbOpration.filter('UrlShortner')

	def findUrlFromDB(self, url):
		return self.dbOpration.filter('UrlShortner',{'short_url':url})

	def generateUniqueCode(self):
		return uuid.uuid4()