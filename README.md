# EmployeeManagement

Template app for django microservice

### Folder Structure
```
.
├── Dockerfile
├── README.md
├── apps
│   ├── __init__.py
│   ├── asgi.py
│   ├── employee_management
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── dapr.yaml
├── db.sqlite3
├── local.yml
├── manage.py
├── pyproject.toml
├── requirements.txt
└── setup.cfg

```

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
python manage.py createsuperuser
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
mypy apps/employee_management
```

#### Running tests with Pytest

```
python manage.py test apps.employee_management.tests
```
### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

```commandline

coverage run -m pytest
coverage html
open htmlcov/index.html
```

### DAPR
#### Installation

```
brew install dapr/tap/dapr-cli
dapr init

```
