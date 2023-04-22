from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
# Change it on release - CORS(app, resources={r"/*": {"origins": "http://example.com"}})
CORS(app)


class Home(Resource):
    def get(self):
        return {'message': 'Hello, World!'}, 200


api.add_resource(Home, '/')

if __name__ == "__main__":
    app.run(debug=True, port=8393)
