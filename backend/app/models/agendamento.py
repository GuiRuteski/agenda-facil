from datetime import datetime
from enum import Enum
from app.extensions import db

class StatusAgendamento(Enum):
    AGENDADO = 'agendado'
    CONFIRMADO = 'confirmado'
    CANCELADO = 'cancelado'
    CONCLUIDO = 'concluído'
    FALTOU = 'faltou'

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'
    
    id = db.Column(db.Integer, primary_key=True)
    data_hora = db.Column(db.DateTime, nullable=False)
    duracao = db.Column(db.Integer, default=30, nullable=False)  # em minutos
    status = db.Column(db.Enum(StatusAgendamento), 
                      default=StatusAgendamento.AGENDADO, 
                      nullable=False)
    observacoes = db.Column(db.Text)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    atualizado_em = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    # Chaves estrangeiras
    paciente_id = db.Column(db.Integer, 
                          db.ForeignKey('pacientes.id'), 
                          nullable=False)
    funcionario_id = db.Column(db.Integer, 
                             db.ForeignKey('funcionarios.id'), 
                             nullable=False)
    
    # Relacionamentos
    paciente = db.relationship('Paciente', back_populates='agendamentos')
    funcionario = db.relationship('Funcionario', back_populates='agendamentos')

    def __repr__(self):
        return f'<Agendamento {self.id} - {self.data_hora.strftime("%d/%m/%Y %H:%M")}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'data_hora': self.data_hora.isoformat(),
            'duracao': self.duracao,
            'status': self.status.value,
            'observacoes': self.observacoes,
            'criado_em': self.criado_em.isoformat(),
            'atualizado_em': self.atualizado_em.isoformat() if self.atualizado_em else None,
            'paciente_id': self.paciente_id,
            'funcionario_id': self.funcionario_id,
            'paciente': {
                'nome': self.paciente.nome,
                'cpf': self.paciente.cpf
            } if self.paciente else None,
            'funcionario': {
                'nome': self.funcionario.nome,
                'especialidade': self.funcionario.especialidade
            } if self.funcionario else None
        }