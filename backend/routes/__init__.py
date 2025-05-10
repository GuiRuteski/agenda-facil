from flask import Flask
from flask_restx import Api
from app.extensions import db, jwt
from routes import user_bp, profissionais_bp  # Corrigido aqui

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta_aqui'
    app.config['UPLOAD_FOLDER'] = 'uploads'  # se estiver usando upload de imagens

    # Inicializa extensões
    db.init_app(app)
    jwt.init_app(app)

    # Swagger opcional com flask_restx
    api = Api(
        app,
        version='1.0',
        title='API Agenda Fácil',
        description='Documentação da API',
        doc='/swagger/'
    )

    # Registra os blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(profissionais_bp)  # Corrigido aqui também

    return app
