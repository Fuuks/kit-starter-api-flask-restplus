from flask_restplus import Resource
from flask import after_this_request

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
