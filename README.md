## Cookiecutter template for microservice 

### How to get started
1. install cookiecutter in local
    ```
    pip3 install cookiecutter
    ```

    > Note: if you get error related to urllib, OpenSSL, NotOpenSSLWarning etc. Please run the following command : `pip3 install urllib3==1.26.6`

2. Run cookiecutter 
    Format: 
    ```
    cookiecutter <link_to_repo/local_folder>
    ```

    GitHub Repo
    ```
    cookiecutter gh:rohit-clootrack/micro-template --checkout cookiecutter
    ```

    Local Repo
    1. Clone this repo
    2. Run the cookiecutter command pointing toward this repo
       ```
       cookiecutter micro-template/
       ```
3. Answer the prompts
    1. Project Name
       - Example: "Employee Management"
    2. Project Slug
       - Example: "employee_management"
    3. Model Name 
        - Name of your primary model, this will create a model and relevant files
        - Example: "employee"  (not "employees", "Employee")
    4. Model name in plural
        - Example: "employees"
    5. App name 
       - This will be used in Docker and DAPR to identify the application
       - Example: "employee_app"
    6. Description
        - This will get populated in the generated README.md

4. Your project repo will be generated
5. Follow the instruction given in the README of the generate project
   - Following are some sample commands to get started with
       1. `cd` into the Generated Repo
       2. `python3 -m venv .venv`
       3. `pip3 install -r requirements.txt`
       4. `python3 manage.py makemigrations`
       5. `python3 manage.py migrate`
       6. run the test command given in the README
          - `cat README.md | grep "manage.py test"`


### Next steps

* Generated code will create 5 endpoints: CRUD APIs and a list API. It will be centered about a Model with three fields (`first_name`, `last_name` and `email`). Test cases & serializer are also designed towards this Model
* As per the need of your project, you can modify the Model, test cases, serializer and endpoints
    * You can add more fields to the Model and run the migration commands to create the new fields in the database
    * You can add more endpoints by adding more functions in the `controller/{name}.py` file
    * You may need to add more test cases in the `tests/{name}.py` file
    * You can add more models by adding more classes in the `models/{name}.py` file
    * You can add more serializers by adding more classes in the `serializers/{name}.py` file
    * You can add more apps by adding more files in the `apps/` folder

### Features
* RESTful APIs
* Standard Error message
* Unit Tests
* Pre-commit hooks
* OpenAPI schema / Swagger
* Pagination -- Limit Offset Count
* Continuous Integration - GitHub Actions



### TODO:
* Add postgres support from default -- currently it points towards sqlite.
* Add `environ` for reading environment variables and separate .env for staging/production.
* Sentry support
