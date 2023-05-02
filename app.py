import os
from flask import Flask, Blueprint
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)  # Create a Flask application instance
ssl_path = os.environ.get('SSL_CERTIFICATE_PATH')

# Create a Blueprint for the API V1
api_bp_v1 = Blueprint('apiV1', __name__, url_prefix='/v1')

### swagger specific ###
swagger_url = '/static/swagger.yaml'
swagger_blueprint = get_swaggerui_blueprint(
    "/swagger",
    swagger_url
)

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
app.register_blueprint(swagger_blueprint)

if __name__ == "__main__":
    ssl_context = (ssl_path + "/my_cert.crt",
                   ssl_path + "/my_cert.key")
    app.run(debug=True, port=8393, ssl_context=ssl_context)
