from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.funcionario import Funcionario
from sqlalchemy.exc import SQLAlchemyError

funcionario_bp = Blueprint('funcionario_bp', __name__, url_prefix='/api/funcionarios')


@funcionario_bp.route('/', methods=['GET'])
def listar_funcionarios():
    """
    Lista todos os funcionários
    ---
    tags:
      - Funcionários
    responses:
      200:
        description: Lista de funcionários retornada com sucesso
    """
    funcionarios = Funcionario.query.all()
    return jsonify([f.to_dict() for f in funcionarios]), 200


@funcionario_bp.route('/', methods=['POST'])
def criar_funcionario():
    """
    Cria um novo funcionário
    ---
    tags:
      - Funcionários
    parameters:
      - in: body
        name: funcionario
        schema:
          type: object
          required:
            - nome
            - tipo
            - telefone
          properties:
            nome:
              type: string
            tipo:
              type: string
              enum: [médico, recepcionista, administrador]
            telefone:
              type: string
            ativo:
              type: boolean
    responses:
      201:
        description: Funcionário criado com sucesso
      400:
        description: Erro ao criar funcionário
    """
    data = request.get_json()
    try:
        novo = Funcionario(
            nome=data['nome'],
            tipo=data['tipo'],
            telefone=data['telefone'],
            ativo=data.get('ativo', True)
        )
        db.session.add(novo)
        db.session.commit()
        return jsonify(novo.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400


@funcionario_bp.route('/<int:id>', methods=['PUT'])
def atualizar_funcionario(id):
    """
    Atualiza os dados de um funcionário
    ---
    tags:
      - Funcionários
    parameters:
      - name: id
        in: path
        required: true
        type: integer
      - in: body
        name: funcionario
        schema:
          type: object
          properties:
            nome:
              type: string
            tipo:
              type: string
              enum: [médico, recepcionista, administrador]
            telefone:
              type: string
            ativo:
              type: boolean
    responses:
      200:
        description: Funcionário atualizado com sucesso
      400:
        description: Erro ao atualizar funcionário
      404:
        description: Funcionário não encontrado
    """
    funcionario = Funcionario.query.get_or_404(id)
    data = request.get_json()
    try:
        funcionario.nome = data.get('nome', funcionario.nome)
        funcionario.tipo = data.get('tipo', funcionario.tipo)
        funcionario.telefone = data.get('telefone', funcionario.telefone)
        funcionario.ativo = data.get('ativo', funcionario.ativo)
        db.session.commit()
        return jsonify({'mensagem': 'Funcionário atualizado com sucesso'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'erro': str(e)}), 400


@funcionario_bp.route('/<int:id>', methods=['DELETE'])
def deletar_funcionario(id):
    """
    Deleta um funcionário pelo ID
    ---
    tags:
      - Funcionários
    parameters:
      - name: id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Funcionário deletado com sucesso
      400:
        description: Erro ao deletar funcionário
      404:
        description: Funcionário não encontrado
    """
    funcionario = Func
