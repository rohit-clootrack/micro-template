from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Departments"


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
