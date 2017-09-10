from database.setting import ENVSetting
from datetime import datetime


class DATA:
	def __init__(self):
		self.env = ENVSetting()
		self.env.generateConnection()
		self.connection = self.env.connection
		self.cur = self.connection.cursor()

	def store(self, url):
		self.cur.execute("insert into url_shortner values('"+url[0]+"','"+url[1]+"', '"+str(0)+"', "+datetime.now()+")")
		self.env.closeConnection()

	def getURL(self, shorturl):
		self.cur.execute("select original_url from url_shortner where short_url = '"+shorturl+"'")
		data = self.cur.fetchall()
		self.env.closeConnection()
		return data

	def checkExistance(self, url):
		self.cur.execute("select short_url from url_shortner where original_url = '"+url+"'")
		data = self.cur.fetchall()
		self.env.closeConnection()
		return data

	def getAllUrl(self):
		self.cur.execute("select * from url_shortner")
		data = self.cur.fetchall()
		self.env.closeConnection()
		return data