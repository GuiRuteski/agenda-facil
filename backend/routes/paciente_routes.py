from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.paciente import Paciente
from sqlalchemy.exc import SQLAlchemyError

paciente_bp = Blueprint('paciente_bp', __name__, url_prefix='/api/pacientes')


@paciente_bp.route('/', methods=['GET'])
def listar_pacientes():
    """
    Lista todos os pacientes
    ---
    tags:
      - Pacientes
    responses:
      200:
        description: Lista de pacientes retornada com sucesso
    """
    pacientes = Paciente.query.all()
    return jsonify([p.to_dict() for p in pacientes]), 200


@paciente_bp.route('/', methods=['POST'])
def criar_paciente():
    """
    Cria um novo paciente
    ---
    tags:
      - Pacientes
    parameters:
      - in: body
        name: paciente
        schema:
          type: object
          required:
            - nome
            - cpf
            - telefone
            - email
          properties:
            nome:
              type: string
            cpf:
              type: string
            telefone:
              type: string
            email:
              type: string
    responses:
      201:
        description: Paciente criado com sucesso
      400:
        description: Erro na criação do paciente
    """
    data = request.get_json()
    try:
        novo = Paciente(
            nome=data['nome'],
            cpf=data['cpf'],
            telefone=data['telefone'],
            email=data['email']
        )
        db.session.add(novo)
        db.session.commit()
        return jsonify(novo.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400


@paciente_bp.route('/<int:id>', methods=['GET'])
def obter_paciente(id):
    """
    Retorna um paciente pelo ID
    ---
    tags:
      - Pacientes
    parameters:
      - name: id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Paciente encontrado
      404:
        description: Paciente não encontrado
    """
    paciente = Paciente.query.get_or_404(id)
    return jsonify(paciente.to_dict()), 200


@paciente_bp.route('/<int:id>', methods=['PUT'])
def atualizar_paciente(id):
    """
    Atualiza os dados de um paciente
    ---
    tags:
      - Pacientes
    parameters:
      - name: id
        in: path
        required: true
        type: integer
      - in: body
        name: paciente
        schema:
          type: object
          properties:
            nome:
              type: string
            cpf:
              type: string
            telefone:
              type: string
            email:
              type: string
    responses:
      200:
        description: Paciente atualizado com sucesso
      400:
        description: Erro ao atualizar paciente
      404:
        description: Paciente não encontrado
    """
    paciente = Paciente.query.get_or_404(id)
    data = request.get_json()
    try:
        paciente.nome = data.get('nome', paciente.nome)
        paciente.cpf = data.get('cpf', paciente.cpf)
        paciente.telefone = data.get('telefone', paciente.telefone)
        paciente.email = data.get('email', paciente.email)
        db.session.commit()
        return jsonify({'mensagem': 'Paciente atualizado com sucesso'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400


@paciente_bp.route('/<int:id>', methods=['DELETE'])
def deletar_paciente(id):
    """
    Deleta um paciente pelo ID
    ---
    tags:
      - Pacientes
    parameters:
      - name: id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Paciente deletado com sucesso
      400:
        description: Erro ao deletar paciente
      404:
        description: Paciente não encontrado
    """
    paciente = Paciente.query.get_or_404(id)
    try:
        db.session.delete(paciente)
        db.session.commit()
        return jsonify({'mensagem': 'Paciente deletado com sucesso'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400
