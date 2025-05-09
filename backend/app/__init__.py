from flask import Flask
from flask_cors import CORS
from app.extensions import db, migrate, jwt
from app.config import Config

from routes.user import user_bp
from routes.paciente_routes import paciente_bp
from routes.funcionario_routes import funcionario_bp
from routes.agendamento_routes import agendamento_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Extensões
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(paciente_bp)
    app.register_blueprint(funcionario_bp)
    app.register_blueprint(agendamento_bp)

    return app
