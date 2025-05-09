from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(256), nullable=False)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionarios.id'))

    funcionario = db.relationship('Funcionario', back_populates='usuario')  # <-- ADICIONADO

    def __repr__(self):
        return f'<Usuario {self.email}>'
    
    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)
    
    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'funcionario_id': self.funcionario_id
        }
