# agenda-facil
Agenda Fácil é um sistema completo de agendamento de consultas médicas, desenvolvido com Vue.js 3 no frontend e Flask no backend, utilizando MySQL para persistência de dados.
O projeto é focado em segurança, praticidade e escalabilidade.

TECNOLOGIAS APRESENTADAS
BACKEND:
Flask
Flask-CORS
Flask-JWT-Extended
SQLAlchemy
MySQL

FRONTEND:
Vue.js 3
Vue Router
Vuex
Axios

ESTRUTURA DO PROJETO
BACKEND (/backend)
app.py: Ponto de entrada principal.
run.py: Inicializa a aplicação Flask.
agenda_facil/:
models.py: Define as tabelas (Agendamento, Profissional, Paciente, Usuario).
routes.py: Define as rotas da API para autenticação e CRUD.
config.py: Configurações de banco de dados.
__init__.py: Inicializa a aplicação Flask, banco de dados e JWT.

FRONTEND (/frontend)
src/:
views/:
LoginView.vue: Tela de login.
RegisterView.vue: Tela de cadastro.
Painel.vue: Painel do usuário autenticado.
HomeView.vue: Página inicial.
router/: Configurações de rotas protegidas.
store/: Vuex para gerenciamento de estado.
public/: HTML base.

COMO RODA O PROJETO
Pré-requisitos
Node.js e npm
Python 3
MySQL Server

FUNCIONALIDADES
Cadastro e login de usuários com autenticação JWT.
Proteção de rotas sensíveis para usuários autenticados.
CRUD completo de agendamentos, profissionais e pacientes.
Relacionamento entre entidades no banco de dados.
Armazenamento seguro de senhas (hash).
Interface amigável para login, cadastro e gerenciamento de consultas.

OBJETIVO
O Agenda Fácil tem como objetivo simplificar o processo de agendamento de consultas médicas, proporcionando uma experiência eficiente e segura tanto para pacientes quanto para profissionais.

AUTOR
Projeto desenvolvido por:
- Guilherme Ruteski
- Vinicius Colucci
- Luis Otavio
- Tainara