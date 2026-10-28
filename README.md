# InstaCode API

API backend do **InstaCode**, um aplicativo mobile inspirado no Instagram. Este repositório contém a API REST em Python/Flask responsável por posts, usuários, curtidas e comentários consumida pelo app.

Frontend (React Native): [github.com/DhenzelNxs/InstaCode](https://github.com/DhenzelNxs/InstaCode)

> API própria feita com Python e Flask.

## Stack

- **Flask** — framework web
- **Flask-SQLAlchemy** — ORM
- **SQLite** — banco de dados (arquivo local `app.db`, criado automaticamente)
- **Flask-CORS** — liberação de CORS para o app consumir a API
- **Gunicorn** — servidor WSGI para rodar em produção

Não há autenticação (tokens/JWT) implementada — login é feito apenas conferindo e-mail/senha salvos em texto puro no banco.

## Endpoints

Prefixo base: `/api`

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/posts` | Lista todos os posts, com comentários e curtidas |
| `POST` | `/posts` | Cria um post (aceita `comments` e `liked_by` já no corpo) |
| `GET` | `/posts/getpost/<post_id>` | Retorna um post pelo índice |
| `PATCH` | `/posts/patchpost/<post_id>` | Substitui os comentários de um post |
| `PATCH` | `/posts/likeaction/<post_id>/<action>` | Curtir (`like`) ou descurtir (`deslike`) um post |
| `GET` | `/comments/<post_id>` | Lista os comentários de um post |
| `GET` | `/users` | Lista todos os usuários |
| `POST` | `/users` | Cria um usuário |
| `GET` | `/users/getposts/<nickname>` | Busca os posts de um usuário pelo nickname |
| `PATCH` | `/update_profile_image/<user_id>` | Atualiza a foto de perfil do usuário |

## Como rodar localmente

Pré-requisitos: Python 3.

```bash
# clonar o repositório
git clone https://github.com/DhenzelNxs/InstaCode-api.git
cd InstaCode-api

# criar e ativar um ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# instalar as dependências
pip install -r requirements.txt

# subir a API
python app.py
```

A API fica disponível em `http://localhost:5000/api`. O banco SQLite (`app.db`) é criado automaticamente na primeira execução, sem necessidade de variáveis de ambiente ou configuração adicional.

Para rodar em produção, use o Gunicorn (já incluso em `requirements.txt`):

```bash
gunicorn app:app
```
