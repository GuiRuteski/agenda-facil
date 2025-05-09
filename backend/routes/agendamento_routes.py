from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.agendamento import Agendamento
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

agendamento_bp = Blueprint('agendamento_bp', __name__, url_prefix='/api/agendamentos')

@agendamento_bp.route('/', methods=['GET'])
def listar_agendamentos():
    agendamentos = Agendamento.query.all()
    return jsonify([a.to_dict() for a in agendamentos]), 200

@agendamento_bp.route('/', methods=['POST'])
def criar_agendamento():
    data = request.get_json()
    try:
        novo = Agendamento(
            paciente_id=data['paciente_id'],
            profissional_id=data['profissional_id'],
            data_hora=datetime.strptime(data['data_hora'], "%Y-%m-%dT%H:%M"),
            status=data.get('status', 'Agendado')
        )
        db.session.add(novo)
        db.session.commit()
        return jsonify(novo.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400
