from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, timedelta
from app.models import (
    Agendamento, 
    StatusAgendamento, 
    Paciente, 
    Funcionario, 
    Usuario
)
from app.extensions import db

bp = Blueprint('agendamento', __name__, url_prefix='/api/agendamentos')

@bp.route('/', methods=['POST'])
@jwt_required()
def criar_agendamento():
    dados = request.get_json()
    
    # Validação dos campos obrigatórios
    campos_obrigatorios = ['data_hora', 'paciente_id', 'funcionario_id']
    if not all(campo in dados for campo in campos_obrigatorios):
        return jsonify({'erro': f'Campos obrigatórios faltando: {", ".join(campos_obrigatorios)}'}), 400
    
    # Verifica se paciente e funcionário existem
    paciente = Paciente.query.get(dados['paciente_id'])
    if not paciente or not paciente.ativo:
        return jsonify({'erro': 'Paciente não encontrado ou inativo'}), 404
    
    funcionario = Funcionario.query.get(dados['funcionario_id'])
    if not funcionario or not funcionario.ativo:
        return jsonify({'erro': 'Funcionário não encontrado ou inativo'}), 404
    
    # Converte e valida a data/hora
    try:
        data_hora = datetime.fromisoformat(dados['data_hora'])
        if data_hora < datetime.now():
            return jsonify({'erro': 'Não é possível agendar para datas passadas'}), 400
    except ValueError:
        return jsonify({'erro': 'Formato de data/hora inválido. Use ISO format (YYYY-MM-DDTHH:MM:SS)'}), 400
    
    # Valida a duração
    duracao = dados.get('duracao', 30)
    if not isinstance(duracao, int) or duracao <= 0:
        return jsonify({'erro': 'Duração deve ser um número inteiro positivo'}), 400
    
    # Verifica conflitos de horário
    fim = data_hora + timedelta(minutes=duracao)
    
    conflitos = Agendamento.query.filter(
        Agendamento.funcionario_id == dados['funcionario_id'],
        Agendamento.data_hora < fim,
        Agendamento.data_hora + timedelta(minutes=Agendamento.duracao) > data_hora,
        Agendamento.status != StatusAgendamento.CANCELADO
    ).count()
    
    if conflitos > 0:
        return jsonify({'erro': 'Conflito de horário com outro agendamento'}), 409
    
    # Cria o agendamento
    novo_agendamento = Agendamento(
        data_hora=data_hora,
        duracao=duracao,
        paciente_id=dados['paciente_id'],
        funcionario_id=dados['funcionario_id'],
        observacoes=dados.get('observacoes'),
        status=StatusAgendamento.AGENDADO
    )
    
    db.session.add(novo_agendamento)
    db.session.commit()
    
    return jsonify(novo_agendamento.to_dict()), 201

@bp.route('/', methods=['GET'])
@jwt_required()
def listar_agendamentos():
    # Obtém o usuário atual
    current_user = get_jwt_identity()
    usuario = Usuario.query.filter_by(email=current_user).first()
    
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404
    
    # Inicia a query
    query = Agendamento.query
    
    # Se for funcionário (não admin), filtra apenas seus agendamentos
    if usuario.funcionario and usuario.funcionario.tipo != TipoFuncionario.ADMINISTRADOR:
        query = query.filter(Agendamento.funcionario_id == usuario.funcionario.id)
    
    # Aplica filtros
    data_inicio = request.args.get('data_inicio')
    if data_inicio:
        try:
            query = query.filter(Agendamento.data_hora >= datetime.fromisoformat(data_inicio))
        except ValueError:
            return jsonify({'erro': 'Formato de data_inicio inválido. Use ISO format'}), 400
    
    data_fim = request.args.get('data_fim')
    if data_fim:
        try:
            query = query.filter(Agendamento.data_hora <= datetime.fromisoformat(data_fim))
        except ValueError:
            return jsonify({'erro': 'Formato de data_fim inválido. Use ISO format'}), 400
    
    if 'paciente_id' in request.args:
        query = query.filter(Agendamento.paciente_id == request.args['paciente_id'])
    
    if 'funcionario_id' in request.args:
        query = query.filter(Agendamento.funcionario_id == request.args['funcionario_id'])
    
    if 'status' in request.args:
        try:
            query = query.filter(Agendamento.status == StatusAgendamento(request.args['status']))
        except ValueError:
            return jsonify({'erro': 'Status inválido'}), 400
    
    # Ordena e executa a query
    agendamentos = query.order_by(Agendamento.data_hora.asc()).all()
    return jsonify([ag.to_dict() for ag in agendamentos])

@bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def obter_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    return jsonify(agendamento.to_dict())

@bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def atualizar_agendamento(id):
    current_user = get_jwt_identity()
    usuario = Usuario.query.filter_by(email=current_user).first()
    
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404
    
    agendamento = Agendamento.query.get_or_404(id)
    dados = request.get_json()
    
    # Verifica permissões
    if (usuario.funcionario and 
        usuario.funcionario.id != agendamento.funcionario_id and
        usuario.funcionario.tipo != TipoFuncionario.ADMINISTRADOR):
        return jsonify({'erro': 'Acesso não autorizado'}), 403
    
    # Atualiza campos permitidos
    if 'data_hora' in dados:
        try:
            agendamento.data_hora = datetime.fromisoformat(dados['data_hora'])
        except ValueError:
            return jsonify({'erro': 'Formato de data/hora inválido'}), 400
    
    if 'duracao' in dados:
        agendamento.duracao = dados['duracao']
    
    if 'observacoes' in dados:
        agendamento.observacoes = dados['observacoes']
    
    if 'status' in dados:
        try:
            agendamento.status = StatusAgendamento(dados['status'])
        except ValueError:
            return jsonify({'erro': 'Status inválido'}), 400
    
    db.session.commit()
    return jsonify(agendamento.to_dict())

@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def cancelar_agendamento(id):
    current_user = get_jwt_identity()
    usuario = Usuario.query.filter_by(email=current_user).first()
    
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado'}), 404
    
    agendamento = Agendamento.query.get_or_404(id)
    
    # Verifica permissões
    if (usuario.funcionario and 
        usuario.funcionario.id != agendamento.funcionario_id and
        usuario.funcionario.tipo != TipoFuncionario.ADMINISTRADOR):
        return jsonify({'erro': 'Acesso não autorizado'}), 403
    
    # Marca como cancelado em vez de deletar
    agendamento.status = StatusAgendamento.CANCELADO
    db.session.commit()
    
    return jsonify({'mensagem': 'Agendamento cancelado com sucesso'}), 200