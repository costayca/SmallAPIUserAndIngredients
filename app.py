import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from resources.errors import errors
from dotenv import load_dotenv, find_dotenv
from flask_mail import Mail

app = Flask(__name__)

load_dotenv(find_dotenv())
app.config.update(
    SECRET_KEY=os.environ.get("JWT_SECRET_KEY")
)

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
mail = Mail(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}

initialize_db(app)
initialize_routes(api)

app.run()