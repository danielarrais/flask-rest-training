from flask import Flask
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)


videos = {}


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("likes", type=int, help="Likes of the video")
video_put_args.add_argument("name", type=str, help="Name of the video")
video_put_args.add_argument("views", type=int, help="Views of the video")


class Video(Resource):
    def get(self, video_id):
        return videos[video_id], 200

    def put(self, video_id):
        args = video_put_args.parse_args()
        return {video_id: args}


class HelloWord(Resource):
    def get(self, name):
        return {
            "data": {
                "name": name
            }
        }


api.add_resource(HelloWord, "/helloworld/<string:name>")
api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__":
    app.run(debug=True)
