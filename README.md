# wsBackendFabricaDeSoftware26.2

Backend de um **e-commerce desenvolvido com Django e Django REST Framework**, criado como projeto da disciplina **Fábrica de Software 26.2 – Workshop de Backend**.

O projeto implementa uma API REST para gerenciamento de produtos, categorias, pedidos, itens de pedidos e endereços, além de uma interface HTML simples para interação com os produtos.

---

## 📋 Sobre o projeto

O sistema foi desenvolvido com foco nos principais conceitos de desenvolvimento backend utilizando Django:

- CRUD completo;
- Relacionamentos entre entidades através de chaves estrangeiras;
- API REST;
- Autenticação utilizando JWT;
- Consumo de API externa;
- Tratamento de erros;
- Documentação da API com Swagger/OpenAPI;
- Banco de dados SQLite3;
- Interface HTML simples para interação com o sistema;
- Organização do projeto;
- Versionamento utilizando Git e commits semânticos.

---

## 🎯 Requisitos do projeto

### Obrigatórios

- [x] Projeto Django
- [x] CRUD completo
- [x] Duas ou mais entidades relacionadas
- [x] Relacionamentos utilizando chave estrangeira
- [x] Consumo de API externa gratuita
- [x] Tratamento de erros
- [x] `.gitignore`
- [x] `requirements.txt`
- [x] `README.md`
- [x] Repositório `wsBackendFabricaDeSoftware26.2`

### Diferenciais implementados

- [x] Organização de diretórios
- [x] Boas práticas de desenvolvimento
- [x] Commits semânticos
- [x] Documentação da API
- [x] GitHub
- [x] Página funcional em HTML/CSS
- [x] Autenticação utilizando JWT
- [x] Swagger/OpenAPI

### Não utilizado

- [ ] Docker Compose
- [ ] Banco de dados externo MySQL/PostgreSQL

O banco utilizado nesta versão é o **SQLite3**, integrado ao Django, para manter o projeto simples e facilitar sua execução em diferentes computadores.

---

# 🛠️ Tecnologias utilizadas

- **Python 3.13**
- **Django 6.1**
- **Django REST Framework**
- **Simple JWT**
- **DRF Spectacular**
- **SQLite3**
- **HTML5**
- **CSS3**
- **JavaScript**
- **Git**
- **GitHub**

---

# 📁 Estrutura do projeto

```text
wsBackendFabricaDeSoftware26.2/
│
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── services.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

> A pasta `venv/` é utilizada apenas no ambiente local de desenvolvimento e não deve ser enviada ao GitHub.

---

# 🗃️ Modelagem do sistema

## Categoria

Representa as categorias disponíveis na loja. Uma categoria pode possuir vários produtos.

## Produto

Representa os produtos disponíveis para venda, contendo informações como nome, descrição, preço, estoque e categoria.

Relacionamento:

```text
Category
    │
    │ 1:N
    ▼
Product
```

## Pedido

Representa um pedido realizado por um usuário autenticado.

```text
User
  │
  │ 1:N
  ▼
Order
```

## Item do pedido

Representa os produtos pertencentes a um pedido.

```text
Order
  │
  │ 1:N
  ▼
OrderItem
```

## Endereço

Representa um endereço associado ao usuário.

```text
User
  │
  │ 1:N
  ▼
Address
```

---

# 🔗 Relacionamentos

```text
Category
   │
   └──────────< Product


User
   │
   ├──────────< Order
   │
   └──────────< Address


Order
   │
   └──────────< OrderItem
                    │
                    └──── Product
```

---

# 🔐 Autenticação

A API utiliza **JWT (JSON Web Token)** para autenticação.

O processo básico é:

```text
Usuário
   │
   ▼
Login
   │
   ▼
JWT
   │
   ▼
Requisições autenticadas
   │
   ▼
API
```

## Login

```text
POST /api/auth/login/
```

Exemplo:

```json
{
    "username": "usuario",
    "password": "senha"
}
```

## Atualização do token

```text
POST /api/auth/refresh/
```

## Utilizando o token

Nas requisições protegidas:

```text
Authorization: Bearer SEU_TOKEN
```

---

# 🛍️ API da loja

A API principal utiliza o prefixo:

```text
/api/
```

## Categorias

```text
GET     /api/categories/
POST    /api/categories/
GET     /api/categories/<id>/
PUT     /api/categories/<id>/
PATCH   /api/categories/<id>/
DELETE  /api/categories/<id>/
```

## Produtos

```text
GET     /api/products/
POST    /api/products/
GET     /api/products/<id>/
PUT     /api/products/<id>/
PATCH   /api/products/<id>/
DELETE  /api/products/<id>/
```

Permite consultar, cadastrar, atualizar e excluir produtos.

## Pedidos

```text
GET     /api/orders/
POST    /api/orders/
GET     /api/orders/<id>/
PUT     /api/orders/<id>/
PATCH   /api/orders/<id>/
DELETE  /api/orders/<id>/
```

Os pedidos são relacionados ao usuário autenticado.

## Itens dos pedidos

```text
GET     /api/order-items/
POST    /api/order-items/
GET     /api/order-items/<id>/
PUT     /api/order-items/<id>/
PATCH   /api/order-items/<id>/
DELETE  /api/order-items/<id>/
```

## Endereços

```text
GET     /api/addresses/
POST    /api/addresses/
GET     /api/addresses/<id>/
PUT     /api/addresses/<id>/
PATCH   /api/addresses/<id>/
DELETE  /api/addresses/<id>/
```

---

# 📮 Consulta de CEP

O sistema possui um endpoint para consulta de CEP através de uma API externa gratuita:

```text
GET /api/cep/<cep>/
```

O sistema realiza a consulta e retorna os dados encontrados.

Caso o CEP seja inválido:

```json
{
    "detail": "CEP inválido."
}
```

O consumo possui tratamento de erros e verificação da resposta HTTP.

---

# 📖 Swagger / OpenAPI

A API possui documentação automática através do **DRF Spectacular**.

## Swagger

```text
http://127.0.0.1:8000/api/docs/
```

A documentação interativa permite visualizar e testar os endpoints.

## Schema OpenAPI

```text
http://127.0.0.1:8000/api/schema/
```

---

# 🖥️ Interface web

O projeto possui uma interface HTML simples para facilitar a interação com a aplicação.

A página inicial:

```text
http://127.0.0.1:8000/
```

A interface permite:

- Visualização dos produtos;
- Cadastro de produtos;
- Exclusão de produtos;
- Interação com a API;
- Autenticação para utilização dos recursos protegidos.

Foi desenvolvida utilizando HTML, CSS e JavaScript.

---

# ⚙️ Instalação e execução

## 1. Pré-requisitos

É necessário possuir:

- Python 3.13 ou compatível;
- Git;
- Navegador web.

Não é necessário instalar MySQL ou PostgreSQL, pois o projeto utiliza SQLite3.

## 2. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/wsBackendFabricaDeSoftware26.2.git
cd wsBackendFabricaDeSoftware26.2
```

> Substitua `SEU-USUARIO` pelo seu usuário do GitHub.

## 3. Criar o ambiente virtual

No Windows:

```powershell
python -m venv venv
```

## 4. Ativar o ambiente virtual

```powershell
.\venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie scripts:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Depois:

```powershell
.\venv\Scripts\Activate.ps1
```

## 5. Instalar dependências

```powershell
python -m pip install -r requirements.txt
```

## 6. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```dotenv
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
```

> A `SECRET_KEY` pode ser qualquer string longa e aleatória para uso em desenvolvimento. Como o projeto utiliza o SQLite3 padrão do Django, não é necessário configurar variáveis de banco de dados externo.

## 7. Aplicar migrations

```powershell
python manage.py migrate
```

## 8. Verificar o projeto

```powershell
python manage.py check
```

Resultado esperado:

```text
System check identified no issues (0 silenced).
```

## 9. Criar superusuário

```powershell
python manage.py createsuperuser
```

Informe username, e-mail e senha.

## 10. Iniciar o servidor

```powershell
python manage.py runserver
```

A aplicação estará disponível em:

```text
http://127.0.0.1:8000/
```

---

# 🌐 URLs principais

| Recurso | URL |
|---|---|
| Interface | `http://127.0.0.1:8000/` |
| Admin | `http://127.0.0.1:8000/admin/` |
| API | `http://127.0.0.1:8000/api/` |
| Categorias | `http://127.0.0.1:8000/api/categories/` |
| Produtos | `http://127.0.0.1:8000/api/products/` |
| Pedidos | `http://127.0.0.1:8000/api/orders/` |
| Itens de pedidos | `http://127.0.0.1:8000/api/order-items/` |
| Endereços | `http://127.0.0.1:8000/api/addresses/` |
| Consulta de CEP | `http://127.0.0.1:8000/api/cep/<cep>/` |
| Login | `http://127.0.0.1:8000/api/auth/login/` |
| Renovação JWT | `http://127.0.0.1:8000/api/auth/refresh/` |
| Schema | `http://127.0.0.1:8000/api/schema/` |
| Swagger | `http://127.0.0.1:8000/api/docs/` |

---

# 🧪 Testando a aplicação

A sequência recomendada é:

### 1. Criar usuário

Utilize o Django Admin ou o mecanismo de autenticação configurado.

### 2. Realizar login

```text
POST /api/auth/login/
```

Obtenha o token JWT.

### 3. Criar uma categoria

```text
POST /api/categories/
```

Exemplo:

```json
{
    "name": "Eletrônicos",
    "description": "Produtos eletrônicos"
}
```

### 4. Criar um produto

```text
POST /api/products/
```

Exemplo:

```json
{
    "name": "Mouse Gamer",
    "description": "Mouse para jogos",
    "price": "99.90",
    "stock": 10,
    "category": 1
}
```

### 5. Consultar produtos

```text
GET /api/products/
```

### 6. Atualizar um produto

```text
PUT /api/products/<id>/
```

ou:

```text
PATCH /api/products/<id>/
```

### 7. Excluir um produto

```text
DELETE /api/products/<id>/
```

---

# 🗄️ Banco de dados

O projeto utiliza **SQLite3**, integrado ao Django.

O arquivo do banco é:

```text
db.sqlite3
```

Não é necessário configurar um servidor MySQL ou PostgreSQL para executar o projeto.

---

# 🔄 Migrations

Quando houver alterações nos modelos:

```powershell
python manage.py makemigrations
```

Depois:

```powershell
python manage.py migrate
```

---

# 🔀 Git e commits semânticos

O projeto utiliza Git para controle de versão e commits semânticos.

Exemplos:

```text
feat: adiciona cadastro de produtos
fix: corrige cadastro de produtos
chore: configura ambiente do projeto
docs: adiciona documentacao do projeto
refactor: reorganiza estrutura da api
test: adiciona testes para produtos
```

| Tipo | Utilização |
|---|---|
| `feat` | Nova funcionalidade |
| `fix` | Correção de erro |
| `docs` | Documentação |
| `refactor` | Refatoração |
| `chore` | Configurações/manutenção |
| `test` | Testes |

---

# 🚫 Arquivos ignorados pelo Git

O projeto utiliza `.gitignore` para evitar o versionamento de arquivos locais.

Entre eles:

```text
venv/
```

Também devem ser evitados arquivos temporários e informações sensíveis.

---

# 🔒 Segurança

A autenticação dos endpoints protegidos utiliza JWT.

Os tokens de autenticação **não devem ser adicionados ao código-fonte ou ao README**.

Também não devem ser publicados:

- Senhas;
- Tokens;
- Chaves secretas;
- Credenciais;
- Informações privadas.

Em produção, configurações sensíveis devem ser armazenadas de maneira segura, preferencialmente utilizando variáveis de ambiente.

---

# 📚 Arquitetura simplificada

```text
                 USUÁRIO
                    │
                    ▼
             Interface HTML
                    │
                    ▼
              Django / DRF
                    │
        ┌───────────┼────────────┐
        │           │            │
        ▼           ▼            ▼
   Produtos    Categorias     Pedidos
        │           │            │
        └───────────┼────────────┘
                    │
                    ▼
                SQLite3
                    │
                    ▼
             Banco de dados
```

Consulta de CEP:

```text
Usuário
   │
   ▼
Django
   │
   ▼
Serviço de CEP
   │
   ▼
Resultado
```

---

# 🧩 Funcionalidades

## Produtos

- Cadastro;
- Consulta;
- Atualização;
- Exclusão;
- Controle de estoque;
- Associação com categoria.

## Categorias

- Cadastro;
- Consulta;
- Atualização;
- Exclusão.

## Pedidos

- Criação;
- Consulta;
- Atualização;
- Exclusão;
- Associação ao usuário.

## Itens de pedidos

- Cadastro;
- Consulta;
- Atualização;
- Exclusão;
- Associação com pedido e produto.

## Endereços

- Cadastro;
- Consulta;
- Atualização;
- Exclusão;
- Associação ao usuário.

## CEP

- Consulta através de API externa;
- Tratamento de CEP inválido;
- Retorno das informações obtidas pelo serviço externo.

## Autenticação

- Login;
- Token JWT;
- Renovação do token;
- Proteção de endpoints.

---

# 📌 Considerações finais

O projeto foi desenvolvido como uma aplicação backend de e-commerce com Django, demonstrando na prática conceitos fundamentais de desenvolvimento de APIs REST.

A aplicação possui:

- Modelagem de dados;
- Relacionamentos entre entidades;
- Operações CRUD;
- Autenticação;
- Integração com API externa;
- Tratamento de erros;
- Documentação através de Swagger;
- Interface web funcional;
- Banco de dados SQLite3;
- Versionamento com Git;
- Commits semânticos;
- Organização de código e diretórios.

O projeto pode ser executado localmente seguindo as etapas apresentadas neste documento, sem a necessidade de configuração de um banco de dados externo ou Docker.

---

## 👨‍🎓 Projeto acadêmico

**Projeto:** wsBackendFabricaDeSoftware26.2  
**Disciplina:** Fábrica de Software 26.2 – Workshop de Backend  
**Tecnologias principais:** Python, Django, Django REST Framework e SQLite3  
**Objetivo:** Desenvolvimento de uma aplicação backend de e-commerce com API REST, autenticação, relacionamentos, integração externa e documentação.