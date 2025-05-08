from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models.paciente import Paciente
from app import db

bp = Blueprint('paciente', __name__, url_prefix='/api/pacientes')

@bp.route('/', methods=['GET'])
@jwt_required()
def listar_pacientes():
    pacientes = Paciente.query.all()
    return jsonify([p.to_dict() for p in pacientes])

@bp.route('/', methods=['POST'])
@jwt_required()
def criar_paciente():
    dados = request.get_json()
    
    paciente = Paciente(
        nome=dados['nome'],
        cpf=dados['cpf'],
        telefone=dados.get('telefone'),
        email=dados.get('email'),
        data_nascimento=dados.get('data_nascimento')
    )
    
    db.session.add(paciente)
    db.session.commit()
    
    return jsonify(paciente.to_dict()), 201