from app.extensions import db
from datetime import datetime

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'

    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    status = db.Column(
        db.Enum('Agendado', 'Cancelado', 'Concluído', name='status_enum'),
        default='Agendado',
        nullable=False
    )
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    paciente = db.relationship('Paciente', backref='agendamentos')
    medico = db.relationship('Medico', backref='agendamentos')

