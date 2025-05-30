from app import create_app
from app.extensions import db
from sqlalchemy import text
from app.models import Paciente, Funcionario, Agendamento  # Certifique-se que estão no __init__.py dos models

app = create_app()

with app.app_context():
    try:
        result = db.session.execute(text('SELECT 1'))
        print("✅ Conexão bem-sucedida com o banco de dados.")
    except Exception as e:
        print("❌ Erro ao conectar ao banco:", e)
