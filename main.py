from flask import Flask
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)


class HelloWord(Resource):
    def get(self):
        return {"data": "Hello World"}


api.add_resource(HelloWord, "/helloworld")


if __name__ == "__main__":
    app.run(debug=True)
