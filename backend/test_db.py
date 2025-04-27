from agenda_facil import create_app, db
from sqlalchemy import text
from models import Paciente, Funcionario, Agendamento

app = create_app()

with app.app_context():
    # Utilizando text() corretamente
    result = db.session.execute(text('SELECT 1'))
    print("Conexão bem-sucedida:", result)
