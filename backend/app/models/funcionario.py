from app.extensions import db
from datetime import datetime
from enum import Enum
from werkzeug.security import generate_password_hash, check_password_hash

class TipoFuncionario(Enum):
    SECRETARIA = 'secretaria'
    ADMINISTRADOR = 'administrador'
    RECEPCIONISTA = 'recepcionista'

class Funcionario(db.Model):
    __tablename__ = 'funcionarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    tipo = db.Column(db.Enum(TipoFuncionario), nullable=False)
    especialidade = db.Column(db.String(100))
    senha = db.Column(db.String(512), nullable=False)
    sexo = db.Column(db.String(10))  # ou Enum se preferir


    ativo = db.Column(db.Boolean, default=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha, senha)
