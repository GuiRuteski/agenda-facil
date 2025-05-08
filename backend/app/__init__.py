from flask import Flask
from .config import Config  # Importação relativa corrigida

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Inicializa extensões
    from .extensions import db, migrate, jwt
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Registra blueprints
    from routes import user, paciente, funcionario, agendamento
    app.register_blueprint(user.bp)
    app.register_blueprint(paciente.bp)
    app.register_blueprint(funcionario.bp)
    app.register_blueprint(agendamento.bp)
    
    return app