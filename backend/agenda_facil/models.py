from app import db  # Já que o arquivo app.py está na raiz do diretório backend


class Paciente(db.Model):
    __tablename__ = 'pacientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    telefone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)  # Adicionando senha para o paciente
    tipo = db.Column(db.String(20), default='paciente')  # Tipo padrão como 'paciente' 
    

    def __init__(self, nome, cpf, telefone, email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.senha = None
        self.tipo = 'paciente'

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'telefone': self.telefone,
            'email': self.email
        }

    def __repr__(self):
        return f'<Paciente {self.nome}>'
    
    agendamentos = db.relationship('Agendamento', backref='paciente', lazy=True)
    

class Funcionario(db.Model):
    __tablename__ = 'funcionarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)

    agendamentos = db.relationship('Agendamento', backref='funcionario', lazy=True)

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'

    id = db.Column(db.Integer, primary_key=True)
    data_agendamento = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default='pendente')
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionarios.id'), nullable=True)
