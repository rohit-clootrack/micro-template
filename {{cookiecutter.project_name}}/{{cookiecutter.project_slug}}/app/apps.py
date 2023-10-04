from django.apps import AppConfig


class {{cookiecutter.model_name|title}}ManagementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{cookiecutter.project_slug}}.app"
