from rest_framework import renderers, serializers

from {{cookiecutter.project_slug}}.app.models.{{cookiecutter.model_name}} import {{cookiecutter.model_name|title}}


class {{cookiecutter.model_name|title}}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {{cookiecutter.model_name|title}}
        fields = "__all__"


# To have custom response format -- we can use the standard serializer
class StandardResponseSerializer(serializers.Serializer):
    status = serializers.CharField(default="success")
    response = serializers.DictField()
    message = serializers.CharField(allow_null=True, default=None)


# To have custom response format -- we can use the custom renderer
class CustomRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {"status": "success", "response": data, "message": None}
        return super().render(response_data, accepted_media_type, renderer_context)
