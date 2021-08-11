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

Essa aplicação poder ser execudada de duas formas:

- Uso dos programas Python e Postgres da sua máquina
- Uso de docker

---

### Rodar Sem Docker

Faça suas migrations:

```bash
python manage.py makemigrations
```

Crie suas tabelas no SQLite:

```bash
python manage.py migrate
```

Rode o servidor dos apps do Django na rota localhost:8000

```bash
python manage.py runserver
```

---

### Rodar Com Docker

---

## Features

MagPy API é uma aplicação Api Rest para o gerenciamento de projetos python com as seguintes features:

- **Listar Projetos:**: todos os projetos serão retornados em forma de lista com seus pacotes devidamente cadastrados.

- **Criar Projeto:**: é possível criar um projeto es seus pacotes, caso o pacote não tenha versão, será fornecido a versão mais recente.

- **Atualizar Nome:** caso tenha passado o nome do projeto errado é possível fazer a alteração do nome sem alterar os pacotes contidos nele.

- **Deletar Projeto:** é possível excluir um projeto cadastro de acordo com a solicitação do usuário.

## Uso e Documentação

Essa Api foi documetada com _[swagger][swagger]_ e acessada via --MinhaRota--/docs/ URL

Também tem acesso aos endpoints da api através do _[postman][postman]_

## Rotas da API

### /api/projects **Method GET**

Essa rota retorna a lista de projetos cadastrados.

## Release

- 0.1.0
  - Public release

## Autor

- Gustavo Henrique Messias _[GustavoM96 GitHub URL][github]_

[postman]: https://www.postman.com/api-platform/
[github]: https://github.com/GustavoM96
[swagger]: https://swagger.io/
[heroku]: https://www.heroku.com/platform
[postgresql]: https://www.postgresql.org/
[sqlite]: https://www.sqlite.org/index.html
[python]: https://www.python.org/download/releases/3.0/
[django]: https://docs.djangoproject.com/en/2.1/releases/2.0/
[django_rest]: https://www.django-rest-framework.org/
