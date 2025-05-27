from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.funcionario import Funcionario
from werkzeug.security import generate_password_hash

# Removido url_prefix='/api' para evitar duplicação na rota final
funcionario_bp = Blueprint('funcionario', __name__)

@funcionario_bp.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    funcionarios = Funcionario.query.all()
    resultado = [
        {
            'id': f.id,
            'nome': f.nome,
            'email': f.email,
            'cpf': f.cpf,
            'telefone': f.telefone,
            'tipo': f.tipo.value,
            'especialidade': f.especialidade
        } for f in funcionarios
    ]
    return jsonify(funcionarios=resultado)

@funcionario_bp.route('/funcionarios', methods=['POST'])
def criar_funcionario():
    data = request.get_json()

    funcionario = Funcionario(
        nome=data['nome'],
        email=data['email'],
        senha=generate_password_hash(data['senha']),
        cpf=data['cpf'],
        telefone=data.get('telefone'),
        tipo=data['tipo'],
        especialidade=data.get('especialidade')
    )

    db.session.add(funcionario)
    db.session.commit()

    return jsonify({'id': funcionario.id, 'nome': funcionario.nome}), 201
