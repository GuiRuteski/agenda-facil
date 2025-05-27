from flask import Blueprint

# Blueprint principal agrupando os outros
routes_bp = Blueprint('routes', __name__)

# Importa os blueprints individuais
from routes.user import user_bp
from routes.paciente_routes import paciente_bp
from routes.medico_routes import medico_bp
from routes.funcionario_routes import funcionario_bp
from routes.auth_routes import auth_bp

# Registro dos blueprints SEM prefixos redundantes
routes_bp.register_blueprint(user_bp)
routes_bp.register_blueprint(paciente_bp)
routes_bp.register_blueprint(medico_bp)
routes_bp.register_blueprint(funcionario_bp)
routes_bp.register_blueprint(auth_bp)  # <- já possui /api/auth internamente
