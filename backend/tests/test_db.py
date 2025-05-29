from app import create_app, db

# Crie uma aplicação de teste
app = create_app()

# Teste a conexão com o banco de dados
with app.app_context():
    try:
        db.create_all()  # Cria as tabelas no banco de dados
        print("Conexão com o banco de dados foi bem-sucedida!")
    except Exception as e:
        print(f"Erro na conexão com o banco de dados: {e}")
