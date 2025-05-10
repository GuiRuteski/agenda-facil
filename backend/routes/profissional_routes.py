from flask import request, jsonify, Blueprint, current_app
from flask_jwt_extended import jwt_required
from app import db
from app.models.profissional import Profissional

from werkzeug.utils import secure_filename
import os
from datetime import datetime

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

profissionais_bp = Blueprint('profissionais', __name__, url_prefix='/profissionais')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@profissionais_bp.route('', methods=['GET'])
@jwt_required()
def listar_profissionais():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    especialidade = request.args.get('especialidade')
    ativo = request.args.get('ativo', type=lambda v: v.lower() == 'true')

    query = Profissional.query

    if especialidade:
        query = query.filter(Profissional.especialidade.ilike(f'%{especialidade}%'))
    
    if ativo is not None:
        query = query.filter(Profissional.ativo == ativo)

    profissionais = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        'items': [p.to_dict() for p in profissionais.items],
        'total': profissionais.total,
        'pages': profissionais.pages,
        'current_page': page
    })

@profissionais_bp.route('', methods=['POST'])
@jwt_required()
def criar_profissional():
    dados = request.get_json()
    
    if Profissional.query.filter_by(nome=dados['nome']).first():
        return jsonify({'message': 'Já existe um profissional com este nome'}), 400

    novo = Profissional(
        nome=dados['nome'],
        especialidade=dados['especialidade'],
        ativo=dados.get('ativo', True)
    )
    
    db.session.add(novo)
    db.session.commit()
    return jsonify(novo.to_dict()), 201

@profissionais_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def atualizar_profissional(id):
    profissional = Profissional.query.get_or_404(id)
    dados = request.get_json()

    if 'nome' in dados and dados['nome'] != profissional.nome:
        if Profissional.query.filter_by(nome=dados['nome']).first():
            return jsonify({'message': 'Nome já está em uso'}), 400

    profissional.nome = dados.get('nome', profissional.nome)
    profissional.especialidade = dados.get('especialidade', profissional.especialidade)
    profissional.ativo = dados.get('ativo', profissional.ativo)
    profissional.updated_at = datetime.utcnow()
    
    db.session.commit()
    return jsonify(profissional.to_dict())

@profissionais_bp.route('/<int:id>/foto', methods=['POST'])
@jwt_required()
def upload_foto(id):
    profissional = Profissional.query.get_or_404(id)
    
    if 'foto' not in request.files:
        return jsonify({'message': 'Nenhum arquivo enviado'}), 400
        
    file = request.files['foto']
    if file.filename == '':
        return jsonify({'message': 'Nome de arquivo inválido'}), 400
        
    if file and allowed_file(file.filename):
        filename = secure_filename(f"prof_{id}_{datetime.now().timestamp()}.{file.filename.split('.')[-1]}")
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        profissional.foto_url = f"/uploads/{filename}"
        db.session.commit()
        
        return jsonify({'foto_url': profissional.foto_url})
    
    return jsonify({'message': 'Tipo de arquivo não permitido'}), 400