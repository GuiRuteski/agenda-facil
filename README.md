# 🗓️ Agenda Fácil

Agenda Fácil é um sistema completo de agendamentos médicos, desenvolvido com **Vue.js** no frontend, **Flask** no backend e **MySQL** como banco de dados. Ele permite que pacientes, médicos e recepcionistas interajam por meio de um painel intuitivo, com funcionalidades como login seguro, cadastro, agendamentos dinâmicos e exibição de consultas agendadas.

---

## 🚀 Funcionalidades

- ✅ Cadastro e login com autenticação JWT
- ✅ Diferenciação de usuários (Paciente, Médico, Recepcionista)
- ✅ Painel inicial personalizado conforme o tipo de usuário
- ✅ Agendamentos com data, horário e profissional
- ✅ Listagem dinâmica da agenda na página inicial
- ✅ Integração completa entre frontend e backend
- ✅ Documentação via Swagger (Flasgger)
- ✅ Proteção de rotas e persistência de sessão

---

## 🛠️ Tecnologias Utilizadas

| Camada     | Ferramentas / Frameworks           |
|------------|------------------------------------|
| **Frontend** | Vue.js, Axios, CSS Modules        |
| **Backend**  | Python, Flask, SQLAlchemy, JWT, Flasgger |
| **Banco**    | MySQL                             |
| **Outros**   | Flask-Migrate, dotenv, CORS       |

---

## 📁 Estrutura do Projeto
agenda-facil/
├── backend/
│ ├── app/
│ │ ├── models/
│ │ ├── routes/
│ │ ├── extensions.py
│ │ └── init.py
│ ├── run.py
│ ├── .flaskenv
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ │ ├── views/
│ │ ├── assets/
│ │ ├── services/
│ │ ├── router/
│ │ └── App.vue
│ └── package.json


---

## 🧑‍💻 Equipe de Desenvolvimento

| Nome                   | Função                                  |
|------------------------|------------------------------------------|
| **Guilherme Ruteski**  | Desenvolvimento Frontend & Integração   |
| **Vinicius Collucci**  | Backend & Integração com Banco de Dados |
| **Luís Otávio Roveiro**| Autenticação e Estruturação JWT         |
| **Tainara Mariana**    | Documentação, Modelagem e Suporte Lógico|

---

## ⚙️ Como Executar o Projeto

### 🔙 Backend (Flask)

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
flask db upgrade
flask run

### 🔙 Frontend (Vue.js)
cd frontend
npm install
npm run serve

Documentação da API

Acesse via navegador em: http://localhost:5000/apidocs
Documentação gerada automaticamente com o Flasgger (Swagger UI)

Próximas Funcionalidades

Filtros na Agenda (futuros, passados, cancelados)
Upload de imagem de perfil para usuários
Sistema de notificações
Confirmação e cancelamento de agendamentos
Dashboard com relatórios
