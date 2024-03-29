# ![Logo](https://pypi.org/static/images/logo-small.95de8436.svg) MagPy API

## Proposta da MagPy

Para o gerenciamento de projetos python é importante saber quais pacotes são utilizados e em quias versões estão. Porém esses pacotes podem não apresentar sua versão, sabendo que quando isso ocorre é porque ela usa a versão mais atual.

Para esse problema foi desenvolvido uma Api para gerenciar projetos e seus pacotes com as versões utilizadas. No exemplo abaixo exemplifica a solução com o projeto Titan com o pacote Django sem versão.

**PROJETO TITAN**

    {
        "name": "titan",
        "packages": [
            {"name": "Django",},
            {"name": "graphene", "version": "2.0"}
        ]
    }

ao aplicar esse projeto na MagPy API Django recebe a versão "3.2.5"

    {
        "name": "titan",
        "packages": [
            {"name": "Django","version": "3.2.5"},// versão atual
            {"name": "graphene", "version": "2.0"}
        ]
    }

## Tech

MagPy API usou as seguintes tecnologias:

- **Database-Produção:** _[PostgreSQL][postgresql]_
- **Database-Desenvolvimento:** _[SQLite][sqlite]_
- **Backend:** _[Python][python]_ + _[Django][django]_ + _[Django Rest][django_rest]_;
- **Deploy:** _[Heroku][heroku]_

## Como rodar a aplicação

Essa aplicação poder ser executada de três formas:

- Ambiente de testes
- Uso dos programas Python e Postgres da sua máquina
- Uso de docker

---

### Rodar Testes

exporte a variável de ambiente TEST=TEST em seu ambiente:

```bash
export TEST=TEST
```

---

### Rodar Sem Docker

Faça suas migrations:

```bash
python manage.py makemigrations
```

Crie suas tabelas no Banco de dados:

```bash
python manage.py migrate
```

Rode o servidor dos apps do Django na rota localhost:8000:

```bash
python manage.py runserver
```

---

### Rodar Com Docker

crie um volume para fazer a ponte entre o container e o host(sua máquina):

```bash
docker volume create --name=magpy
```

Para a criação dos containers utilizados construa a imagem magpy:

```bash
docker build . --tag magpy
```

construa os container com docker-compose:

```bash
docker-compose up
```

Com outro terminal, acesse o shell do conatiner utilizado execute o comando:

```bash
docker exec -it teste-python-jr-remoto-2021-06_web_1 /bin/bash
```

Após estar no bash do container, faça as migrations:

```bash
python manage.py migrate
```

---

## Features

MagPy API é uma aplicação Api Rest para o gerenciamento de projetos python com as seguintes features:

- **Listar Projetos:** todos os projetos serão retornados em forma de lista com seus pacotes devidamente cadastrados.

- **Pegar Projetos Por Nome:** Ao solicitar o nome do projeto por url, é retornado este com seus dados.

- **Criar Projeto:** é possível criar um projeto es seus pacotes, caso o pacote não tenha versão, será fornecido a versão mais recente.

- **Deletar Projeto:** é possível excluir um projeto cadastro de acordo com a solicitação do usuário.

Erros tradados citados na lista abaixo:

- **Cadastrar projetos com pacotes inválidos:** todos os projetos a serem cadastrados devem ter seus pacotes corretamente cadastrados na _[Pypi][pypi]_,com nome e versão corretamente.

- **Cadastrar projetos já existente:** Caso um projeto a ser cadastrado tenha o seu nome já registrado, será retornado uma mensagem de erro e o cadastro será cancelado.

## Features Extras

features extras que contém no projeto:

- **Atualizar Nome:** caso tenha passado o nome do projeto errado é possível fazer a alteração do nome sem alterar os pacotes contidos nele.

- Relacionamento das tabelas project e packageRelease ManyToMany para a não repetição de pacotes com a mesma versão.
  <img src="images/MagPy.png" alt="relação de tabelas">

- Implementação de Docker, Docker-compose para isolamento do sistemas operacionais, programas e pacotes.

- Teste Unitários: Testado Models, Services e Views com o framework _[django Rest][django_rest]_ com cobertura de 99% reportado nos arquivos report_test.txt e report_coverage.txt encontrados na pasta raiz deste projeto.

- Testes automatizados com CI/CD do GitLab.
  <img src="images/ci-cd.png" alt="ci-cd">

## Uso e Documentação

Essa api está hospedada no _[Heroku][heroku]_ nesse link -> _[magpy-gustavo-messias.com][url_magpy]_

Essa Api foi documentada com _[swagger][swagger]_ e acessada via _[magpy-gustavo-messias.com DOCS][url_magpy]_

Também tem acesso aos endpoints da api através do _[postman][postman]_ com o link da _[documentação postman URL][postman_api]_

## Rotas da API

### /api/projects **Method GET**

    Listar Projetos

<img src="images/list.png" alt="image crud">

---

### /api/projects/{name} **Method GET**

    Pegar Projeto pelo nome

<img src="images/retrieve.png" alt="image crud">

---

### /api/projects/ **Method POST**

    Criar Projeto

<img src="images/create.png" alt="image crud">

---

### /api/projects/{name} **Method PATCH**

    Alterar apenas o nome do projeto

<img src="images/update.png" alt="image crud">

---

### /api/projects/{name} **Method DELETE**

    Deletar um projeto pelo nome

<img src="images/delete.png" alt="image crud">

---

## Rotas que retornam Erros

### /api/projects/ **Method Post**

    Criar projeto já existente.

<img src="images/name-error.png" alt="image crud error">

---

### /api/projects/ **Method Post**

    Cadastrar pacote inválido.

<img src="images/package-error.png" alt="image crud error">

---

## Release

- 0.1.0
  - Public release

## Autores

- Gustavo Henrique Messias _[GustavoM96 GitHub URL][github]_
- Instruct _[Instruct GitHub URL][instruct]_

[url_magpy]: https://magpy-gustavo-messias.herokuapp.com/
[instruct]: https://github.com/instruct-br
[pypi]: https://pypi.org/
[postman_api]: https://documenter.getpostman.com/view/16886916/Tzz5uJoe#4cbc5fad-951c-4a8f-a2ff-6257dbbd42db
[postman]: https://www.postman.com/api-platform/
[github]: https://github.com/GustavoM96
[swagger]: https://swagger.io/
[heroku]: https://www.heroku.com/platform
[postgresql]: https://www.postgresql.org/
[sqlite]: https://www.sqlite.org/index.html
[python]: https://www.python.org/download/releases/3.0/
[django]: https://docs.djangoproject.com/en/2.1/releases/2.0/
[django_rest]: https://www.django-rest-framework.org/
