from app import create_app
from app.extensions import db
from flask_migrate import Migrate
from app import models# importa os modelos (Paciente, Medico etc)

app = create_app()
migrate = Migrate(app, db)

with app.app_context():
    print('\n🔗 Rotas disponíveis:')
    for rule in app.url_map.iter_rules():
        print(f'{rule.methods} -> {rule}')
