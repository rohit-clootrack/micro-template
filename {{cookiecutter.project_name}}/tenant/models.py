from django.db import models
from django_tenants.models import DomainMixin, TenantMixin


class Tenant(TenantMixin):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tenant"


class Domain(DomainMixin):
    pass
