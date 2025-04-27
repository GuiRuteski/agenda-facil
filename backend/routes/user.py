from flask import Blueprint, request, jsonify

user_bp = Blueprint('user', __name__)

@user_bp.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, rota funcionando!"})
