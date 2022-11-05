from flask import Flask
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)


class HelloWord(Resource):
    def get(self, name):
        return {
            "data": {
                "name": name
            }
        }


api.add_resource(HelloWord, "/helloworld/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)
