from flask_restplus import Resource
from flask import after_this_request

class HelloWorld(Resource):
    def get(self):

        @after_this_request
        def set_cookie(response):
            response.set_cookie('user','Papa',max_age=64800,httponly=False)
            return response

        return {'hello': 'world'}
