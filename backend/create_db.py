from app import create_app
from app.extensions import db  # Adicione este import

app = create_app()

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso!")