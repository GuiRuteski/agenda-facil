from .paciente import Paciente  # Apenas importa a classe Paciente
from . import db  # Certifique-se de que o db foi importado aqui sem causar cíclicos

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.models.paciente import Paciente
