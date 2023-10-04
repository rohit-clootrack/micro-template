from django.contrib import admin

from {{cookiecutter.project_slug}}.app.models.{{cookiecutter.model_name}} import {{cookiecutter.model_name|title}}


@admin.register({{cookiecutter.model_name|title}})
class {{cookiecutter.model_name|title}}Admin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")


