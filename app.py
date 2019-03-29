from flask import Flask
from flask_restplus import Resource, Api
from ressources.hello_world import HelloWorld
from ressources.person import Person

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/hello', '/world')
api.add_resource(Person, '/person')


if __name__ == '__main__':
    app.run(debug=True)