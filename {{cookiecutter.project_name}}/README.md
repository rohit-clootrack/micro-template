# {{cookiecutter.project_name}}

{{cookiecutter.description}}

### Folder Structure
```
.
├── Dockerfile
├── README.md
├── TODO.md
├── dapr.yaml
├── db.sqlite3
├── {{cookiecutter.project_slug}}
│   ├── __init__.py
│   ├── app
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── config.py
│   │   ├── controllers
│   │   │   ├── __init__.py
│   │   │   └── {{cookiecutter.model_name}}.py
│   │   ├── db_interface
│   │   │   ├── __init__.py
│   │   │   └── {{cookiecutter.model_name}}.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── {{cookiecutter.model_name}}.py
│   │   ├── serializers
│   │   │   ├── __init__.py
│   │   │   └── {{cookiecutter.model_name}}.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   └── {{cookiecutter.model_name}}.py
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── errors.py
│   │       ├── config.py
│   │       ├── pagination.py
│   │       └── logger.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── local.yml
├── manage.py
├── pyproject.toml
├── requirements.txt
└── setup.cfg
```
### Features
* RESTful APIs
* Standard Error message
* Unit Tests
* Pre-commit hooks
* OpenAPI schema / Swagger
* Custom Pagination -- Limit Offset Count
* Continuous Integration - GitHub Actions
* Logger


### Endpoints
* GET `/api/v1.0/{{cookiecutter.model_name_plural}}`
* POST `/api/v1.0/{{cookiecutter.model_name_plural}}`
* GET `/api/v1.0/{{cookiecutter.model_name_plural}}/:id`
* PUT `/api/v1.0/{{cookiecutter.model_name_plural}}/:id`
* DELETE `/api/v1.0/{{cookiecutter.model_name_plural}}/:id`

# Getting Started

## Non-Docker Setup:

#### Create virtual environment and install dependencies
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

#### Migrations
Copy the sample env file and make changes as per the environment
```
cp .env.sample .env
```

Make changes models.py to suit the needs of your app

Generate migration files using the following command
```
python3 manage.py makemigrations
```

Run the migration
```
python3 manage.py migrate
```

#### Setting Up Your Users

To create a **superuser account**, use this command:

```
python3 manage.py createsuperuser
```

#### Run Server
```
python3 manage.py runserver 8000
```
#### Running tests with Pytest

```
python3 manage.py test {{cookiecutter.project_slug}}.app.tests.{{cookiecutter.model_name}}
```


## Docker Setup:

1. Copy the .env file
```
cp .env.sample .env
```

2. Start the docker containers
```
docker-compose -f local.yml up --build
```

3. Shell into django's container
```
docker exec -it neo_{{cookiecutter.project_slug}} bash
```
> Note: If the name "neo_{{cookiecutter.project_slug}}" doesn't match, run `docker ps` and get the name of the django container

4. Make migrations
```
python3 manage.py makemigrations
```

5. Run migrations
```
python3 manage.py migrate
```

6. [Optional] Run tests
```
python3 manage.py test {{cookiecutter.project_slug}}.app.tests.{{cookiecutter.model_name}}
```

7. [Optional] Create superuser for admin access
```
python3 manage.py createsuperuser
```


### Pre-Commit Hooks [Important]
Install pre-commit hook using the following command. After this, pre-commit hooks will be executed everytime you commit the code.
```
pre-commit install
```

Incase, you want to manually trigger the pre-commit hooks
```
pre-commit run all-files
```
#### Type checks

Running type checks with mypy:
```
mypy {{cookiecutter.project_slug}}/app
```


#### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

```commandline

coverage run -m pytest
coverage html
open htmlcov/index.html
```

## DAPR
#### Installation

```
brew install dapr/tap/dapr-cli
dapr init
```
#### Standalone Mode
```
dapr run --app-id {{cookiecutter.app_name}} --app-port 8000 --dapr-http-port 3500 python3 manage.py runserver 8000

```
Make a request:
```commandline
curl http://localhost:3500/v1.0/invoke/{{cookiecutter.app_name}}/method/api/v1.0/{{cookiecutter.model_name_plural}}/
```

#### Kubernetes

* Build Docker Image
```
docker build . -t neo_{{cookiecutter.project_slug}}:latest
```

* Run docker-compose
```
 docker-compose -f local.yml up --build
```
[This section is under construction]

## API References

#### Sample response format
```
{
    "response": {
        "data": {
            "{{cookiecutter.model_name_plural}}": []
        },
    },
    "status": "success",
    "message": null,
}
```

#### Sample Paginated Response
```json
{
    "response": {
        "data": {},
        "pagination": {
            "count": 2,
            "next": "http://localhost:8000/api/v1.0/{{cookiecutter.model_name_plural}}/?limit=1&offset=1",
            "previous": null,
        },
    },
    "status": "success",
    "message": null,
}
```


#### Sample Error response
we are using `drf-standardized-errors` plugin for error response.

* **type** can be `client_error`, `server_error` or `validation_error`
```json
{
    "status": "error",
    "type": "client_error",
    "errors": [
        {
            "code": "not_found",
            "detail": "Not found.",
            "attr": null
        }
    ]
}

```


####  Notes of naming stuff:
* Name Mold : [adjective]_[noun]_[measurement]
  * Example: Suppose you are storing maximum number of order per month. What is the variable name?
    * max_order_length

    [Learn More](https://www.youtube.com/watch?v=z7w2lKG8zWM&t=325s)


#### Swagger Documentation

* Swagger documentation is available at `/api/schema/swagger-ui/` endpoint
* Redoc documentation is available at `/api/schema/redoc/` endpoint
* OpenAPI schema is available at `/api/schema/openapi.json` endpoint
