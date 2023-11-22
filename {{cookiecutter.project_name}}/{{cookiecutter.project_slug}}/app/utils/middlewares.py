from django.db import connection
from django_tenants.middleware import TenantMainMiddleware
from django_tenants.postgresql_backend.base import FakeTenant
from rest_framework.request import Request


def set_custom_schema(request: Request, schema_name: str):
    tenant = FakeTenant(tenant_type=None, schema_name=schema_name)
    tenant.domain_url = schema_name
    request.tenant = tenant
    connection.set_tenant(request.tenant)


class TenantCustomMiddleware(TenantMainMiddleware):
    @staticmethod
    def hostname_from_request(request):
        """Extracts hostname from request. Used for custom requests filtering.
        By default removes the request's port and common prefixes.
        """
        hostname = request.headers.get("X-TENANT-ID", None)
        return hostname

    def process_request(self, request):
        # Connection needs first to be at the public schema, as this is where
        # the tenant metadata is stored.

        hostname = self.hostname_from_request(request)
        if not hostname:
            from django.http import JsonResponse

            return JsonResponse({"error": "X-TENANT-ID header is missing"}, status=401)

        set_custom_schema(request, hostname)
        self.setup_url_routing(request)
