from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from app.extensions import db, jwt

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta_aqui'

    db.init_app(app)
    jwt.init_app(app)

    from routes import user_bp
    app.register_blueprint(user_bp)

    return app
