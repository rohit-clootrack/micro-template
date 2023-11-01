from django.db import models


class MetadataModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    created_by = models.UUIDField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, db_index=True)
    updated_by = models.UUIDField(blank=True, null=True)
    deleted_on = models.DateTimeField(blank=True, null=True, db_index=True)
    deleted_by = models.UUIDField(blank=True, null=True)

    class Meta:
        abstract = True


class {{cookiecutter.model_name | title}}(MetadataModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
