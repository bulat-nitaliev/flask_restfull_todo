import os
from flask import Flask, g
from flask_restful import Api
from settings import user, host, port, database, password
from api.models import db
from api.resources import TodoResource
from flask_swagger_ui import get_swaggerui_blueprint




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}/{database}'
db.init_app(app)
# with app.app_context():
#     db.create_all()

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/openapi.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },

)

app.register_blueprint(swaggerui_blueprint)

todoApi = Api(app)
todoApi.add_resource(TodoResource,
                     '/tasks', '/tasks/<int:todo_id>',
                     endpoint='todos'
                     )


@app.after_request
def after_request(response):
    # Enable CORS
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = \
        'Accept, Content-Type, Origin, X-Requested-With'
    response.headers['Access-Control-Allow-Methods'] = \
        'GET, POST, PUT, OPTIONS, DELETE'
    return response




if __name__ == "__main__":
    app.run(debug=True)
