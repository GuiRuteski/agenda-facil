from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.funcionario import Funcionario, TipoFuncionario
from app.models.user import Usuario
from app import db

bp = Blueprint('funcionario', __name__, url_prefix='/api/funcionarios')

@bp.route('/', methods=['GET'])
@jwt_required()
def listar_funcionarios():
    current_user = get_jwt_identity()
    usuario = Usuario.query.filter_by(email=current_user).first()
    
    if not usuario or not usuario.funcionario:
        return jsonify({'message': 'Acesso negado'}), 403
    
    funcionarios = Funcionario.query.all()
    return jsonify([f.to_dict() for f in funcionarios])

@bp.route('/', methods=['POST'])
@jwt_required()
def criar_funcionario():
    current_user = get_jwt_identity()
    usuario = Usuario.query.filter_by(email=current_user).first()
    
    # Verifica se é administrador
    if not usuario or not usuario.funcionario or usuario.funcionario.tipo != TipoFuncionario.ADMINISTRADOR:
        return jsonify({'message': 'Acesso negado'}), 403
    
    dados = request.get_json()
    
    funcionario = Funcionario(
        nome=dados['nome'],
        cpf=dados['cpf'],
        telefone=dados.get('telefone'),
        email=dados['email'],
        tipo=TipoFuncionario(dados['tipo']),
        especialidade=dados.get('especialidade'),
        ativo=dados.get('ativo', True)
    )
    
    db.session.add(funcionario)
    db.session.commit()
    
    return jsonify(funcionario.to_dict()), 201

@bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def obter_funcionario(id):
    funcionario = Funcionario.query.get_or_404(id)
    return jsonify(funcionario.to_dict())

@bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def atualizar_funcionario(id):
    current_user = get_jwt_identity()
    usuario = Usuario.query.filter_by(email=current_user).first()
    
    if not usuario or not usuario.funcionario:
        return jsonify({'message': 'Acesso negado'}), 403
    
    funcionario = Funcionario.query.get_or_404(id)
    dados = request.get_json()
    
    funcionario.nome = dados.get('nome', funcionario.nome)
    funcionario.telefone = dados.get('telefone', funcionario.telefone)
    funcionario.email = dados.get('email', funcionario.email)
    funcionario.especialidade = dados.get('especialidade', funcionario.especialidade)
    funcionario.ativo = dados.get('ativo', funcionario.ativo)
    
    db.session.commit()
    return jsonify(funcionario.to_dict())

@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def deletar_funcionario(id):
    current_user = get_jwt_identity()
    usuario = Usuario.query.filter_by(email=current_user).first()
    
    if not usuario or not usuario.funcionario or usuario.funcionario.tipo != TipoFuncionario.ADMINISTRADOR:
        return jsonify({'message': 'Acesso negado'}), 403
    
    funcionario = Funcionario.query.get_or_404(id)
    
    # Verifica se há agendamentos futuros
    agendamentos_futuros = any(a for a in funcionario.agendamentos if not a.concluido)
    if agendamentos_futuros:
        return jsonify({'message': 'Não é possível deletar, existem agendamentos futuros'}), 400
    
    # Marca como inativo em vez de deletar
    funcionario.ativo = False
    db.session.commit()
    
    return jsonify({'message': 'Funcionário marcado como inativo'}), 200