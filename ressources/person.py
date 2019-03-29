from flask import request
from flask_restplus import Resource

class Person(Resource):

	def post(self):
		return 	pass

	def get(self):

		if 'user' not in request.cookies:
			return 401
		return request.cookies.get('user')