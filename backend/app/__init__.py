from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger
from flask_migrate import Migrate

from app.extensions import db
from routes import routes_bp  # importa o grupo de blueprints
from routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)

    # Configurações da aplicação
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:365214@localhost:3306/agenda_facil'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'secretao'
    app.config['JWT_IDENTITY_CLAIM'] = 'sub'  # <- IMPORTANTE para funcionar com dicionário no identity
    app.config['SWAGGER'] = {
        'title': 'Agenda Fácil API',
        'uiversion': 3
    }

    # Inicialização das extensões
    db.init_app(app)
    JWTManager(app)

    # Liberação de CORS para o frontend Vue.js
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}}, supports_credentials=True)

    # Documentação automática com Swagger
    Swagger(app)
    
    migrate = Migrate(app, db)

    # Registro do blueprint principal (todos agrupados no routes_bp)
    app.register_blueprint(routes_bp, url_prefix="/api")
    app.register_blueprint(auth_bp)

    # Rota de teste
    @app.route('/hello')
    def hello():
        return "Swagger funcionando!"

    return app
