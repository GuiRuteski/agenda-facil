from app.extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Medico(db.Model):
    __tablename__ = 'medicos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.Text, nullable=False)


    especialidade = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20))

    ativo = db.Column(db.Boolean, default=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha, senha)
