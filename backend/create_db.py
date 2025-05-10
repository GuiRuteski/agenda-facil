from app import create_app
from app.extensions import db

# Cria o app com a factory
app = create_app()

# Cria o contexto da aplicação para acessar as extensões
with app.app_context():
    db.create_all()
    print("Banco de dados criado com sucesso!")
