from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity, get_jwt
)
from app.models.paciente import Paciente
from app.models.medico import Medico
from app.models.funcionario import Funcionario
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    user = (
        Paciente.query.filter_by(email=email).first() or
        Medico.query.filter_by(email=email).first() or
        Funcionario.query.filter_by(email=email).first()
    )

    if not user or not check_password_hash(user.senha, senha):
        return jsonify({'erro': 'Credenciais inválidas'}), 401

    tipo = user.__class__.__name__.lower()

    token = create_access_token(
        identity=str(user.id),
        additional_claims={
            'email': user.email,
            'tipo': tipo
        }
    )

    return jsonify(
    access_token=token,
    tipo=tipo
), 200


@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def perfil():
    user_id = get_jwt_identity()     # apenas o ID
    claims = get_jwt()               # dados extras

    tipo = claims.get('tipo')
    email = claims.get('email')

    if tipo == 'paciente':
        user = Paciente.query.get(int(user_id))
        if user:
            return jsonify({
                'id': user.id,
                'nome': user.nome,
                'email': user.email,
                'cpf': user.cpf,
                'telefone': user.telefone,
                'sexo': user.sexo,
                'tipo': tipo
            }), 200

    elif tipo == 'medico':
        user = Medico.query.get(int(user_id))
        if user:
            return jsonify({
                'id': user.id,
                'nome': user.nome,
                'email': user.email,
                'especialidade': user.especialidade,
                'telefone': user.telefone,
                'tipo': tipo
            }), 200

    elif tipo == 'funcionario':
        user = Funcionario.query.get(int(user_id))
        if user:
            return jsonify({
                'id': user.id,
                'nome': user.nome,
                'email': user.email,
                'telefone': user.telefone,
                'sexo': user.sexo,
                'tipo_funcionario': user.tipo.value,
                'tipo': tipo
            }), 200

    return jsonify({'erro': 'Usuário não encontrado'}), 404
