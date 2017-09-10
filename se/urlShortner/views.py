from flask import request, render_template, jsonify
from flask.views import MethodView
from controllers import *
from seResponse.SeResponse import SeResponse
import json

class Home(MethodView):

	def get(self):
		linklist = urlShorten().myUrlList()
		return render_template('index.html', data = linklist)


class Shortner(MethodView):

	def post(self):
		try:
			urlshort = urlShorten()
			shorted = urlshort.shorturl(request.form['url'])

			# shorted, code, hint = urlshort.shorturl(request.form['url'])
			return SeResponse(data=shorted, code=200).seSuccess()
			# return SeResponse(data=shorted, code=code, hint).seSuccess()
			# _____________ this is for both success & exception __________
			# __________________ No need of try & except __________________
		except Exception as e:
			return SeResponse(code=500, hint=e).seError()

class DisplayShortn(MethodView):
	def get(self, shortnerId):
		try:
			urlshort = urlShorten()
			originalUrl = urlshort.findUrlFromDB(shortnerId)[0]['originalUrl']
			# urlshort.visit(shortnerId)
			return render_template('anotherpage.html', originalUrl = originalUrl)
		except Exception as e:
			return SeResponse(code=500, hint=e).seError()

	def put(self, shortnerId):
		pass

	def delete(self, shortnerId):
		pass
	

class FilterShortner(MethodView):
	def get(self, shortnerId):
		try:
			urlshort = urlShorten()
			# originalUrl = urlshort.findUrlFromDB(request.args.get("shorturl"))
			originalUrl = urlshort.findUrlFromDB(shortnerId)
			return SeResponse(data=originalUrl, code=200).seSuccess()
			# return render_template('anotherpage.html', originalUrl = originalUrl)
		except Exception as e:
			return SeResponse(code=500, hint=e).seError()
