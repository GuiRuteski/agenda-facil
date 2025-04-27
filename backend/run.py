# backend/run.py

from flask import Flask
from flask_jwt_extended import JWTManager
from .agenda_facil.routes.user import user_bp

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'sua-chave-secreta'
jwt = JWTManager(app)

# Registra as rotas do blueprint
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='