from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__, url_prefix='/api')

@user_bp.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, rota funcionando!"})
