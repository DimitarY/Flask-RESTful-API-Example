from flask import Flask, Blueprint
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)  # Create a Flask application instance

# Create a Blueprint for the API
api_bp_v1 = Blueprint('apiV1', __name__, url_prefix='/v1')

# Change it on release - CORS(app, resources={r"/*": {"origins": "http://example.com"}})
CORS(app)

# Creating API instance
apiV1 = Api(api_bp_v1)


class Home(Resource):
    def get(self):
        return {'message': 'Hello, World!'}, 200


apiV1.add_resource(Home, '/')

# Register the Blueprint to the Flask application
app.register_blueprint(api_bp_v1)

if __name__ == "__main__":
    app.run(debug=True, port=8393)
