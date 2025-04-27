from flask import Blueprint, request, jsonify
from app import db
from ..models.paciente import Paciente # type: ignore
from sqlalchemy.exc import SQLAlchemyError

paciente_bp = Blueprint('paciente_bp', __name__)

@paciente_bp.route('/pacientes', methods=['POST'])
def add_paciente():
    data = request.get_json()
    try:
        novo_paciente = Paciente(
            nome=data['nome'],
            cpf=data['cpf'],
            telefone=data['telefone'],
            email=data['email']
        )
        db.session.add(novo_paciente)
        db.session.commit()
        return jsonify({'message': 'Paciente criado com sucesso!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@paciente_bp.route('/pacientes', methods=['GET'])
def get_pacientes():
    pacientes = Paciente.query.all()
    return jsonify([paciente.to_dict() for paciente in pacientes]), 200

@paciente_bp.route('/pacientes/<int:id>', methods=['GET'])
def get_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    return jsonify(paciente.to_dict()), 200

@paciente_bp.route('/pacientes/<int:id>', methods=['PUT'])
def update_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    data = request.get_json()
    try:
        paciente.nome = data.get('nome', paciente.nome)
        paciente.cpf = data.get('cpf', paciente.cpf)
        paciente.telefone = data.get('telefone', paciente.telefone)
        paciente.email = data.get('email', paciente.email)
        db.session.commit()
        return jsonify({'message': 'Paciente atualizado com sucesso!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@paciente_bp.route('/pacientes/<int:id>', methods=['DELETE'])
def delete_paciente(id):
    paciente = Paciente.query.get_or_404(id)
    try:
        db.session.delete(paciente)
        db.session.commit()
        return jsonify({'message': 'Paciente deletado com sucesso!'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
