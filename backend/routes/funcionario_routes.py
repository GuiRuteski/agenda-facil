from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.funcionario import Funcionario
from sqlalchemy.exc import SQLAlchemyError

funcionario_bp = Blueprint('funcionario_bp', __name__, url_prefix='/api/funcionarios')

@funcionario_bp.route('/', methods=['GET'])
def listar_funcionarios():
    funcionarios = Funcionario.query.all()
    return jsonify([f.to_dict() for f in funcionarios]), 200

@funcionario_bp.route('/', methods=['POST'])
def criar_funcionario():
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
