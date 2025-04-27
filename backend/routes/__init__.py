from flask import Flask
from flask_cors import CORS
from routes.user import user_bp  # Não é necessário incluir o 'agenda_facil' no caminho


def create_app():
    app = Flask(__name__)
    CORS(app)  # permite requisições de outros domínios (como o frontend em localhost)

    # registrar rotas
    app.register_blueprint(user_bp, url_prefix="/api")

    return app
