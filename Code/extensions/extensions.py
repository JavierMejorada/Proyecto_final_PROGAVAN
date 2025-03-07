from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db_s = SQLAlchemy()
jwt = JWTManager()
