from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.agendamento import Agendamento
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from datetime import datetime

agendamento_bp = Blueprint('agendamentos', __name__)

@agendamento_bp.route('', methods=['GET'])
@jwt_required()
def listar_agendamentos():
    claims = get_jwt()
    user_id = int(get_jwt_identity())
    tipo = claims.get('tipo')

    if tipo == 'paciente':
        agendamentos = Agendamento.query.filter_by(paciente_id=user_id).all()
    elif tipo == 'medico':
        agendamentos = Agendamento.query.filter_by(medico_id=user_id).all()
    else:
        agendamentos = Agendamento.query.all()

    return jsonify([
        {
            'id': ag.id,
            'paciente_id': ag.paciente_id,
            'medico_id': ag.medico_id,
            'data_hora': ag.data_hora.isoformat(),
            'status': ag.status
        }
        for ag in agendamentos
    ])

@agendamento_bp.route('/agendamentos', methods=['POST'])
@jwt_required()
def criar_agendamento():
    data = request.get_json()
    novo = Agendamento(
        paciente_id=data['paciente_id'],
        medico_id=data['medico_id'],
        data_hora=datetime.fromisoformat(data['data_hora']),
        status='Agendado'
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify({'mensagem': 'Agendamento criado com sucesso'}), 201
