from enum import Enum
from app.extensions import db

class TipoFuncionario(Enum):
    MEDICO = 'médico'
    RECEPCIONISTA = 'recepcionista'
    ADMINISTRADOR = 'administrador'

class Funcionario(db.Model):
    __tablename__ = 'funcionarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True, nullable=False)
    tipo = db.Column(db.Enum(TipoFuncionario), nullable=False)
    especialidade = db.Column(db.String(50))
    ativo = db.Column(db.Boolean, default=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relacionamentos
    agendamentos = db.relationship('Agendamento', 
                                  back_populates='funcionario', 
                                  lazy='dynamic')
    usuario = db.relationship('Usuario', 
                             back_populates='funcionario', 
                             uselist=False,
                             cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Funcionario {self.nome} ({self.tipo.value})>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'telefone': self.telefone,
            'email': self.email,
            'tipo': self.tipo.value,
            'especialidade': self.especialidade,
            'ativo': self.ativo,
            'criado_em': self.criado_em.isoformat()
        }