from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.extensions import db
from app.models.user import Usuario
from app.models.funcionario import Funcionario

user_bp = Blueprint('user', __name__, url_prefix='/api/auth')

@user_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    senha = request.json.get('senha', None)
    
    if not email or not senha:
        return jsonify({"message": "Email e senha são obrigatórios"}), 400
    
    usuario = Usuario.query.filter_by(email=email).first()
    
    if not usuario or not usuario.check_senha(senha):
        return jsonify({"message": "Credenciais inválidas"}), 401
    
    if usuario.funcionario and not usuario.funcionario.ativo:
        return jsonify({"message": "Seu acesso está desativado"}), 403
    
    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    current_user = get_jwt_identity()
    usuario = Usuario.query.filter_by(email=current_user).first()
    
    if not usuario:
        return jsonify({"message": "Usuário não encontrado"}), 404
    
    response = usuario.to_dict()
    
    if usuario.funcionario:
        response['funcionario'] = usuario.funcionario.to_dict()
    
    return jsonify(response), 200

@user_bp.route('/funcionarios/<int:funcionario_id>', methods=['POST'])
@jwt_required()
def criar_usuario_funcionario(funcionario_id):
    current_user = get_jwt_identity()
    usuario_admin = Usuario.query.filter_by(email=current_user).first()
    
    if not usuario_admin or not usuario_admin.funcionario or usuario_admin.funcionario.tipo != 'administrador':
        return jsonify({'message': 'Acesso negado'}), 403
    
    funcionario = Funcionario.query.get_or_404(funcionario_id)
    
    if funcionario.usuario:
        return jsonify({'message': 'Funcionário já possui usuário'}), 400
    
    dados = request.get_json()
    
    if Usuario.query.filter_by(email=dados['email']).first():
        return jsonify({'message': 'Email já está em uso'}), 400
    
    usuario = Usuario(
        email=dados['email'],
        funcionario_id=funcionario.id
    )
    usuario.set_senha(dados['senha'])
    
    db.session.add(usuario)
    db.session.commit()
    
    return jsonify(usuario.to_dict()), 201

@user_bp.route('/alterar-senha', methods=['POST'])
@jwt_required()
def alterar_senha():
    current_user = get_jwt_identity()
    usuario = Usuario.query.filter_by(email=current_user).first()
    
    if not usuario:
        return jsonify({"message": "Usuário não encontrado"}), 404
    
    senha_atual = request.json.get('senha_atual')
    nova_senha = request.json.get('nova_senha')
    
    if not senha_atual or not nova_senha:
        return jsonify({"message": "Senha atual e nova senha são obrigatórias"}), 400
    
    if not usuario.check_senha(senha_atual):
        return jsonify({"message": "Senha atual incorreta"}), 400
    
    usuario.set_senha(nova_senha)
    db.session.commit()
    
    return jsonify({"message": "Senha alterada com sucesso"}), 200
