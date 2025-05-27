from app.extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # paciente, medico, secretaria
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def set_senha(self, senha_plana):
        self.senha = generate_password_hash(senha_plana)

    def verificar_senha(self, senha_plana):
        return check_password_hash(self.senha, senha_plana)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "role": self.role
        }
