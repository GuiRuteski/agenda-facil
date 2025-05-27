from flask import Blueprint, jsonify, request

agendamento_bp = Blueprint('agendamento', __name__)

agendamentos = [
    {"id": 1, "descricao": "Consulta com Dr. João"}
]

@agendamento_bp.route('/agendamentos', methods=['GET'])
def listar_agendamentos():
    """
    Lista de agendamentos.
    ---
    tags:
      - Agendamentos
    responses:
      200:
        description: Agendamentos encontrados
    """
    return jsonify({"agendamentos": agendamentos})

@agendamento_bp.route('/agendamentos', methods=['POST'])
def criar_agendamento():
    """
    Cria um novo agendamento.
    ---
    tags:
      - Agendamentos
    parameters:
        - in: body
          name: body
          schema:
            type: object
            properties:
              descricao:
                type: string
    responses:
        201:
          description: Agendamento criado
    """
    data = request.get_json()
    novo = {"id": len(agendamentos)+1, "descricao": data["descricao"]}
    agendamentos.append(novo)
    return jsonify(novo), 201

@agendamento_bp.route('/agendamentos/<int:id>', methods=['PUT'])
def atualizar_agendamento(id):
    """
    Atualiza um agendamento.
    ---
    tags:
      - Agendamentos
    parameters:
        - in: path
          name: id
          type: integer
        - in: body
          name: body
          schema:
            type: object
            properties:
              descricao:
                type: string
    responses:
        200:
          description: Agendamento atualizado
    """
    data = request.get_json()
    for a in agendamentos:
        if a["id"] == id:
            a["descricao"] = data["descricao"]
            return jsonify(a)
    return jsonify({"erro": "Agendamento não encontrado"}), 404

@agendamento_bp.route('/agendamentos/<int:id>', methods=['DELETE'])
def deletar_agendamento(id):
    """
    Deleta um agendamento.
    ---
    tags:
      - Agendamentos
    parameters:
        - in: path
          name: id
          type: integer
    responses:
        200:
          description: Agendamento removido
    """
    global agendamentos
    agendamentos = [a for a in agendamentos if a["id"] != id]
    return jsonify({"mensagem": "Agendamento removido"})
