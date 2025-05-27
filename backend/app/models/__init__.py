from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importa os modelos para o contexto da aplicação
from .usuario import Usuario
from .paciente import Paciente
from .medico import Medico
from .funcionario import Funcionario
from .agendamento import Agendamento
