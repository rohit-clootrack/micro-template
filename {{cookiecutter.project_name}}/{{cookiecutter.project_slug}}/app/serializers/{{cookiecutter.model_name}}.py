from rest_framework import renderers, serializers

from {{cookiecutter.project_slug}}.app.models.{{cookiecutter.model_name}} import {{cookiecutter.model_name|title}}


class {{cookiecutter.model_name|title}}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {{cookiecutter.model_name|title}}
        fields = "__all__"
        exclude = ["created_on", "created_by", "updated_on", "updated_by", "deleted_on", "deleted_by", "is_deleted"]
