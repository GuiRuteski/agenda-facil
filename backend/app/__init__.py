from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicialize o objeto db de forma global para a aplicação
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/agenda_facil'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)  # Passa a app para o db

    return app
