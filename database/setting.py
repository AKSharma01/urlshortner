import env
import psycopg2, psycopg2.extras

class ENVSetting:

	def __init__(self):
		self.connection = ''
		self.uname = self.password = self.host = self.dbname = ''

	def getPGSetting(self):
		self.uname = getattr(env,env.ENV+'pg_uname')
		self.password = getattr(env,env.ENV+'pg_password')
		self.host = getattr(env,env.ENV+'pg_host')
		self.dbname = getattr(env,env.ENV+'pg_database')


	def createConnetionLink(self):
		self.getPGSetting()
		return 'postgresql://'+self.uname+':'+self.password+'@'+self.host+'/'+self.dbname
	
	# def generateConnection(self):
	# 	self.getPGSetting()
	# 	db = "dbname=%s user=%s password=%s host=%s"%(self.dbname, self.uname, self.password, self.host)
	# 	# self.con = psycopg2.connect(db)
	# 	self.connection = psycopg2.connect(db)
	# 	self.connection.autocommit = True

	# def closeConnection(self):
	# 	# self.con.close()
	# 	try:
	# 		connection.close()
	# 	except:
	# 		return "Connection can't be closed"