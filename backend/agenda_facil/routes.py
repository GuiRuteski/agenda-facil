from flask import Blueprint, request, jsonify
from .models import Agendamento
from .models import Agendamento, Profissional
from .models import Paciente
from .models import Usuario
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import db

main = Blueprint('main', __name__)

# Criar novo agendamento
@main.route('/agendamentos', methods=['POST'])
def criar_agendamento():
    data = request.json
    novo = Agendamento(
        nome_paciente=data['nome_paciente'],
        profissional=data['profissional'],
        data_hora=data['data_hora'],
        observacoes=data.get('observacoes', '')
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify({'mensagem': 'Agendamento criado com sucesso!'})

# Listar todos os agendamentos
@main.route('/agendamentos', methods=['GET'])
def listar_agendamentos():
    agendamentos = Agendamento.query.all()
    return jsonify([{
        'id': ag.id,
        'nome_paciente': ag.nome_paciente,
        'profissional': ag.profissional,
        'data_hora': ag.data_hora.isoformat(),
        'observacoes': ag.observacoes
    } for ag in agendamentos])
    
    

# Criar novo profissional
@main.route('/profissionais', methods=['POST'])
def criar_profissional():
    data = request.json
    novo = Profissional(
        nome=data['nome'],
        especialidade=data['especialidade'],
        email=data['email'],
        telefone=data.get('telefone'),
        ativo=data.get('ativo', True)
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify({'mensagem': 'Profissional cadastrado com sucesso!'})

# Listar todos os profissionais
@main.route('/profissionais', methods=['GET'])
def listar_profissionais():
    profs = Profissional.query.all()
    return jsonify([{
        'id': p.id,
        'nome': p.nome,
        'especialidade': p.especialidade,
        'email': p.email,
        'telefone': p.telefone,
        'ativo': p.ativo
    } for p in profs])
    


# Criar novo paciente
@main.route('/pacientes', methods=['POST'])
def criar_paciente():
    data = request.json
    novo = Paciente(
        nome=data['nome'],
        email=data['email'],
        telefone=data.get('telefone'),
        data_nascimento=data.get('data_nascimento'),
        historico_medico=data.get('historico_medico', '')
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify({'mensagem': 'Paciente cadastrado com sucesso!'})

# Listar pacientes
@main.route('/pacientes', methods=['GET'])
def listar_pacientes():
    pacientes = Paciente.query.all()
    return jsonify([{
        'id': p.id,
        'nome': p.nome,
        'email': p.email,
        'telefone': p.telefone,
        'data_nascimento': str(p.data_nascimento),
        'historico_medico': p.historico_medico
    } for p in pacientes])
    
@main.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.json
    if Usuario.query.filter_by(email=data['email']).first():
        return jsonify({'erro': 'Email já cadastrado'}), 400

    novo_usuario = Usuario(
        email=data['email'],
        tipo=data['tipo']
    )
    novo_usuario.set_senha(data['senha'])

    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário cadastrado com sucesso!'})

@main.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = Usuario.query.filter_by(email=data['email']).first()

    if not usuario or not usuario.verificar_senha(data['senha']):
        return jsonify({'erro': 'Credenciais inválidas'}), 401

    token = create_access_token(identity={
        'id': usuario.id,
        'email': usuario.email,
        'tipo': usuario.tipo
    })

    return jsonify({'token': token})

main.route('/minha-agenda')
@jwt_required()
def minha_agenda():
    usuario = get_jwt_identity()
    if usuario['tipo'] != 'profissional':
        return jsonify({'erro': 'Acesso negado'}), 403