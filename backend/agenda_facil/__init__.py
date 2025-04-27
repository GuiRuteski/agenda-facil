from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Aqui você configura o banco de dados MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Driver4123!@localhost/agenda_facil'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # Importa as rotas aqui se necessário
        from agenda_facil.routes import user

    return app
