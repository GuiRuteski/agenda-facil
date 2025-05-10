from flask import Flask
from flasgger import Swagger
from app.extensions import db
from routes.user import user_bp
from routes.paciente_routes import paciente_bp
from routes.agendamento_routes import agendamento_bp
from routes.funcionario_routes import funcionario_bp

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/agenda_facil'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'secretao'
    app.config['SWAGGER'] = {
        'title': 'Agenda Fácil API',
        'uiversion': 3
    }

    db.init_app(app)
    Swagger(app)

    # Blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(paciente_bp)
    app.register_blueprint(agendamento_bp)
    app.register_blueprint(funcionario_bp)

    @app.route('/hello')
    def hello():
        """
        Rota de teste
        ---
        responses:
          200:
            description: OK
        """
        return "Swagger funcionando!"

    return app
