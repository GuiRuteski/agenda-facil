from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.agendamento import Agendamento
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

agendamento_bp = Blueprint('agendamento_bp', __name__, url_prefix='/api/agendamentos')


@agendamento_bp.route('/', methods=['GET'])
def listar_agendamentos():
    """
    Lista todos os agendamentos
    ---
    tags:
      - Agendamentos
    responses:
      200:
        description: Lista de agendamentos retornada com sucesso
    """
    agendamentos = Agendamento.query.all()
    return jsonify([a.to_dict() for a in agendamentos]), 200


@agendamento_bp.route('/', methods=['POST'])
def criar_agendamento():
    """
    Cria um novo agendamento
    ---
    tags:
      - Agendamentos
    parameters:
      - in: body
        name: dados
        schema:
          type: object
          required:
            - paciente_id
            - profissional_id
            - data_hora
          properties:
            paciente_id:
              type: integer
            profissional_id:
              type: integer
            data_hora:
              type: string
              example: "2025-06-10T14:30"
            status:
              type: string
              enum: [Agendado, Cancelado, Concluído]
    responses:
      201:
        description: Agendamento criado com sucesso
      400:
        description: Erro ao criar o agendamento
    """
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


@agendamento_bp.route('/<int:id>', methods=['PUT'])
def atualizar_agendamento(id):
    """
    Atualiza os dados de um agendamento
    ---
    tags:
      - Agendamentos
    parameters:
      - name: id
        in: path
        required: true
        type: integer
      - in: body
        name: dados
        schema:
          type: object
          properties:
            data_hora:
              type: string
              example: "2025-06-15T09:00"
            status:
              type: string
              enum: [Agendado, Cancelado, Concluído]
    responses:
      200:
        description: Agendamento atualizado com sucesso
      404:
        description: Agendamento não encontrado
    """
    agendamento = Agendamento.query.get_or_404(id)
    data = request.get_json()

    if 'data_hora' in data:
        agendamento.data_hora = datetime.strptime(data['data_hora'], "%Y-%m-%dT%H:%M")
    if 'status' in data:
        agendamento.status = data['status']

    db.session.commit()
    return jsonify({'mensagem': 'Agendamento atualizado com sucesso'}), 200


@agendamento_bp.route('/<int:id>', methods=['DELETE'])
def deletar_agendamento(id):
    """
    Deleta um agendamento pelo ID
    ---
    tags:
      - Agendamentos
    parameters:
      - name: id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Agendamento deletado com sucesso
      404:
        description: Agendamento não encontrado
    """
    agendamento = Agendamento.query.get_or_404(id)
    db.session.delete(agendamento)
    db.session.commit()
    return jsonify({'mensagem': 'Agendamento deletado com sucesso'}), 200
