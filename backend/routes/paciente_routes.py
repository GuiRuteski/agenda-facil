from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.paciente import Paciente
from werkzeug.security import generate_password_hash

# 🔧 Removido o /api daqui
paciente_bp = Blueprint('paciente', __name__, url_prefix='/pacientes')

@paciente_bp.route('', methods=['POST'])  # só a raiz do prefixo
def criar_paciente():
    data = request.get_json()

    if not all(k in data for k in ('nome', 'email', 'senha', 'cpf')):
        return jsonify({'erro': 'Dados incompletos'}), 400

    if Paciente.query.filter_by(email=data['email']).first():
        return jsonify({'erro': 'Email já existe'}), 400

    if Paciente.query.filter_by(cpf=data['cpf']).first():
        return jsonify({'erro': 'CPF já existe'}), 400

    paciente = Paciente(
        nome=data['nome'],
        email=data['email'],
        senha=generate_password_hash(data['senha']),
        telefone=data.get('telefone'),
        cpf=data['cpf'],
        sexo=data.get('sexo')
    )

    db.session.add(paciente)
    db.session.commit()

    return jsonify({'id': paciente.id, 'nome': paciente.nome}), 201
