from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configurações do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/agenda_facil'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Configurações do Swagger
    app.config['SWAGGER'] = {
        'title': 'Agenda Fácil API',
        'uiversion': 3
    }

    # Inicializar extensões
    db.init_app(app)
    Swagger(app)

    # Registrar rotas
    from app.routes.paciente_routes import paciente_bp  # type: ignore
    from app.routes.user import user_bp  # se você tiver
    app.register_blueprint(paciente_bp)
    app.register_blueprint(user_bp)

    # ✅ Rota de teste com indentação correta
    @app.route('/hello')
    def hello():
        """
        Rota de Teste
        ---
        responses:
          200:
            description: Mensagem simples de sucesso
        """
        return "Olá, Swagger funcionando!"

    return app
