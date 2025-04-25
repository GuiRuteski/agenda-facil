from flask_jwt_extended import JWTManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    CORS(app)

    from .routes import main
    app.register_blueprint(main)
    
    jwt = JWTManager()
    app.config['JWT_SECRET_KEY'] = 'chave-super-secreta'  # troque isso depois por algo seguro
    
    jwt.init_app(app)

    return app