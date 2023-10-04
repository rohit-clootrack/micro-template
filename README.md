## Cookiecutter template for microservice 

### How to get started
1. install cookiecutter in local
```
pip3 install cookiecutter
```

2. Run cookiecutter 
```
cookiecutter <link_to_repo>
```
Github Repo
```
cookiecutter gh:Clootrack/micro-template
```
Local Repo
```
cookiecutter micro-template/
```

3. Answer the prompts
    1. Project Name
    2. Project Slug
    3. Model Name 
        - Name of your primary model, this will create a model and relevant files
    4. Model name in plural
    5. Description
        - This will get populated in the generated README.md


4. Your project repo will be generated
5. Follow the instruction given in the README of the generate project
    1. cd GeneratedRepo
    2. python3 -m venv .venv
    3. pip3 install -r requirements.txt
    4. python3 manage.py makemigrations
    5. python3 manage.py migrate
    6. run the test command given in the README
