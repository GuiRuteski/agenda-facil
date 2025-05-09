from app.extensions import db
from datetime import datetime

class Paciente(db.Model):
    __tablename__ = 'pacientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    data_nascimento = db.Column(db.Date)
    ativo = db.Column(db.Boolean, default=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relacionamentos
    agendamentos = db.relationship('Agendamento', 
                                 back_populates='paciente', 
                                 lazy='dynamic',
                                 cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Paciente {self.nome}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'telefone': self.telefone,
            'email': self.email,
            'data_nascimento': self.data_nascimento.isoformat() if self.data_nascimento else None,
            'ativo': self.ativo,
            'criado_em': self.criado_em.isoformat()
        }