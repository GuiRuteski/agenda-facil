from app.extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Paciente(db.Model):
    __tablename__ = 'pacientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    sexo = db.Column(db.String(20))
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def set_senha(self, senha_plana):
        self.senha = generate_password_hash(senha_plana)

    def verificar_senha(self, senha_plana):
        return check_password_hash(self.senha, senha_plana)
