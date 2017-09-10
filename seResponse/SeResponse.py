from flask import jsonify

# class Error(Exception):

# 	def __init__(self):
# 		pass

class SeResponse():
	
	def __init__(self, code, data='', hint=None):
		self.data = data
		self.code = code
		self.hint = hint

	def seError(self):
		return jsonify({
				"data" : self.data,
				"responseType" : "error",
				"response" :  {
					"code" : self.code,
					"hint" : str(self.hint)
				}
			})

	def seSuccess(self):
		return jsonify({
				"data" : self.data,
				"responseType" : "success",
				"response" :  {
					"code" : self.code,
					"hint" : str(self.hint)
				}
			})