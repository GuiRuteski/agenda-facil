from .user import Usuario
from .paciente import Paciente
from .profissional import Profissional
from .funcionario import Funcionario, TipoFuncionario
# Dentro de app/routes/paciente.py por exemplo:
from app.models.agendamento import Agendamento, StatusAgendamento

__all__ = [
    'Usuario',
    'Paciente',
    'Funcionario',
    'TipoFuncionario',
    'Agendamento',
    'StatusAgendamento'
]