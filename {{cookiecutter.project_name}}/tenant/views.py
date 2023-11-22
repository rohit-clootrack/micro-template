from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from {{cookiecutter.project_slug}}.app.utils.middlewares import set_custom_schema
from {{cookiecutter.project_slug}}.app.utils.responses import StandardResponse

from tenant.models import Domain, Tenant


class TenantSerializer(serializers.Serializer):
    tenant_id = serializers.CharField(max_length=256)
    tenant_name = serializers.CharField(max_length=512)
    tenant_domain = serializers.CharField()


class TenantListCreateAPIView(APIView):
    @staticmethod
    def get(request):
        return StandardResponse({})

    @staticmethod
    def post(request):
        serializer = TenantSerializer(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        validated_data = serializer.validated_data

        set_custom_schema(request, "public")
        try:
            tenant = Tenant(schema_name=validated_data["tenant_id"], name=validated_data["tenant_name"])
            tenant.save()  # This command runs the migrations as well

            domain = Domain()
            domain.domain = validated_data["tenant_domain"]
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()
        except IntegrityError:
            raise ValidationError("Schema already exists")
        return StandardResponse({"schema_id": tenant.id}, status=201, message="Scheam created successfully")
