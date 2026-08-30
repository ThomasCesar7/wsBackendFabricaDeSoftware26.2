# DevStore API

Projeto desenvolvido para a disciplina **Fábrica de Software 26.2** (Workshop de Backend), utilizando **Django** e **Django REST Framework**.

A DevStore é uma API REST de e-commerce com autenticação JWT, CRUD completo de categorias, produtos, pedidos e endereços, além de consulta de CEP via API pública (ViaCEP) integrada a uma tela funcional de cadastro/login.

## Tecnologias utilizadas

- **Python 3.13**
- **Django 6.1**
- **Django REST Framework**
- **djangorestframework-simplejwt** — autenticação via JWT (access e refresh tokens)
- **drf-spectacular** — geração automática de documentação (Swagger/OpenAPI)
- **SQLite** — banco de dados padrão do Django
- **requests** — consumo da API externa ViaCEP
- HTML/CSS/JavaScript puro — tela funcional de login e cadastro

## Funcionalidades

- Cadastro e login de usuários com autenticação JWT
- CRUD completo de:
  - Categorias (`Category`)
  - Produtos (`Product`) — relacionado a uma categoria
  - Pedidos (`Order`) — relacionado ao usuário autenticado
  - Itens do pedido (`OrderItem`) — relacionado a um pedido
  - Endereços (`Address`) — relacionado ao usuário autenticado
- Consulta de CEP via API pública **ViaCEP**, com tratamento de erros para CEP inválido
- Tela funcional (`index.html`) com:
  - Login
  - Cadastro de usuário com preenchimento automático de rua, bairro, cidade e estado a partir do CEP
  - Listagem, criação, edição e exclusão de produtos
- Documentação interativa da API via Swagger

## Estrutura do projeto

```
wsBackendFabricaDeSoftware26.2/
├── accounts/          # App de autenticação (registro, login, JWT)
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── store/             # App principal (categorias, produtos, pedidos, endereços, CEP)
│   ├── models.py
│   ├── serializers.py
│   ├── services.py    # Integração com a API ViaCEP
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── index.html # Tela funcional (login e cadastro)
├── config/            # Configurações gerais do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── manage.py
└── README.md
```

## Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/ThomasCesar7/wsBackendFabricaDeSoftware26.2.git
cd wsBackendFabricaDeSoftware26.2
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Aplique as migrações

```bash
python manage.py migrate
```

### 5. Crie um superusuário (opcional, para acessar o admin)

```bash
python manage.py createsuperuser
```

### 6. Rode o servidor

```bash
python manage.py runserver
```

O projeto estará disponível em `http://127.0.0.1:8000/`.

## Endpoints principais

| Método | Endpoint | Descrição | Autenticação |
|---|---|---|---|
| POST | `/api/auth/register/` | Cadastra um novo usuário | Não |
| POST | `/api/auth/login/` | Realiza login e retorna tokens JWT | Não |
| GET/POST | `/api/categories/` | Lista/cria categorias | Sim |
| GET/PUT/PATCH/DELETE | `/api/categories/{id}/` | Detalha/atualiza/remove categoria | Sim |
| GET/POST | `/api/products/` | Lista/cria produtos | Sim |
| GET/PUT/PATCH/DELETE | `/api/products/{id}/` | Detalha/atualiza/remove produto | Sim |
| GET/POST | `/api/orders/` | Lista/cria pedidos do usuário logado | Sim |
| GET/POST | `/api/order-items/` | Lista/cria itens de pedido | Sim |
| GET/POST | `/api/addresses/` | Lista/cria endereços do usuário logado | Sim |
| GET | `/api/cep/{cep}/` | Consulta endereço via API ViaCEP | Não |

## Documentação da API (Swagger)

Com o servidor rodando, acesse:

```
http://127.0.0.1:8000/api/docs/
```

Lá é possível visualizar e testar todos os endpoints interativamente, incluindo autenticação via JWT (botão **Authorize**, informando apenas o token, sem a palavra "Bearer").

## Autenticação JWT

Após o login, use o `access` token retornado no header `Authorization` das próximas requisições:

```
Authorization: Bearer SEU_ACCESS_TOKEN
```

## Consumo de API externa

O endpoint `/api/cep/{cep}/` consome a API pública gratuita [ViaCEP](https://viacep.com.br/) para retornar dados de endereço (rua, bairro, cidade, estado) a partir de um CEP. Em caso de CEP inválido ou inexistente, a API retorna erro tratado (`400 Bad Request`) com mensagem apropriada.

## Autor

Thomas Cesar