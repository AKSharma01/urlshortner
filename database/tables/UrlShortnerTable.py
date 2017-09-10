from database.Config import db
from sqlalchemy.sql import func
from datetime import datetime

# print sd
class UrlShortner(db.Model):

	__tablename__ = 'url_shortner'
	id =  db.Column(db.String, primary_key=True)
	original_url = db.Column(db.String, unique=True, nullable=False)
	short_url = db.Column(db.String, unique=True, nullable=False)
	no_of_hits = db.Column(db.Integer, default=0)
	created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
	updated_at = db.Column(db.DateTime, nullable=True, onupdate=func.now())
	# deleted_at = db.Column(db.DateTime, nullable=False, onupdate=func.now())


	def __init__(self, **value):
		self.originalUrl = value.original_url
		self.shortUrl = value.short_url
		self.noOfHits = value.no_of_hits

	def transform(self):
		return {
			'id' : self.id,
			'originalUrl' : self.original_url,
			'shortUrl' : self.short_url,
			'noOfHits' : self.no_of_hits,
			'createdAt' : self.created_at,
			'updatedAt' : self.updated_at
		}


#### this is for advance details

# class UrlHit(db.Model):

# 	__tablename__ = 'url_hits'
# 	id = db.Column(db.Column, primary_key=True)
# 	no_of_hits = db.Column(db.Integer, default=0)
# 	ip_address = db.Column(db.String, nullable=False)
# 	hit_time = db.Column(db.DateTime, nullable=False, onupdate=func.now())
# 	created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
# 	updated_at = db.Column(db.DateTime, nullable=False, onupdate=func.now())
# 	