# EmployeeManagement

Template app for django microservice

### Folder Structure
```
.
├── Dockerfile
├── README.md
├── TODO.md
├── dapr.yaml
├── db.sqlite3
├── employee_management
│   ├── __init__.py
│   ├── app
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── config.py
│   │   ├── errors.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   └── views.py
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
* Pagination

### Endpoints
* GET `/api/v1.0/employees`
* POST `/api/v1.0/employees`
* GET `/api/v1.0/employees/:id`
* PUT `/api/v1.0/employees/:id`
* DELETE `/api/v1.0/employees/:id`

## Basic Commands

### Create virtual environment and install dependencies
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

### Run Migrations
```
python3 manage.py migrate
```

### Setting Up Your Users

To create a **superuser account**, use this command:

```
python3 manage.py createsuperuser
```

### Run Server
```
python3 manage.py runserver
```

### Pre-Commit Hooks
Install pre-commit hook using the following command. After this, pre-commit hooks will be executed everytime you commit the code.
```
pre-commit install
```

Incase, you want to manually trigger the pre-commit hooks
```
pre-commit run all-files
```
### Type checks

Running type checks with mypy:
```
mypy employee_management/app
```

#### Running tests with Pytest

```
python manage.py test employee_management.app.tests
```

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

```commandline

coverage run -m pytest
coverage html
open htmlcov/index.html
```

Notes of naming stuff:
* Name Mold : [adjective]_[noun]_[measurement]
  * Example: Suppose you are storing maximum number of order per month. What is the variable name?
    * max_order_length

[Learn More](https://www.youtube.com/watch?v=z7w2lKG8zWM&t=325s)

### DAPR
#### Installation

```
brew install dapr/tap/dapr-cli
dapr init

```
[This section is in Progress]



### API References

#### Sample Paginated Response
```json
{
    "count": 2,
    "next": "http://localhost:8000/api/v1.0/employees/?limit=1&offset=1",
    "previous": null,
    "results": [
        {
            "id": 1,
            "first_name": "test",
            "last_name": "asas",
            "email": "asas@gmail.com",
            "department": null
        }
    ]
}
```


#### Sample Error response
type can be `client_error`, `server_error` or `validation_error`
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
