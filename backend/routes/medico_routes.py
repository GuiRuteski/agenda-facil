from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.medico import Medico
from werkzeug.security import generate_password_hash

medico_bp = Blueprint('medico', __name__,)

@medico_bp.route('/medicos', methods=['GET'])
def listar_medicos():
    medicos = Medico.query.all()
    resultado = [{'id': m.id, 'nome': m.nome, 'email': m.email, 'especialidade': m.especialidade} for m in medicos]
    return jsonify(medicos=resultado)

@medico_bp.route('/medicos', methods=['POST'])
def adicionar_medico():
    data = request.get_json()
    medico = Medico(
        nome=data['nome'],
        email=data['email'],
        senha=generate_password_hash(data['senha']),
        especialidade=data.get('especialidade')
    )
    db.session.add(medico)
    db.session.commit()
    return jsonify({'id': medico.id, 'nome': medico.nome}), 201
