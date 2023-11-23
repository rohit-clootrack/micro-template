from django.test import Client
from django.urls import reverse
from rest_framework import status
from django_tenants.test.cases import TenantTestCase

from {{cookiecutter.project_slug}}.app.models.{{cookiecutter.model_name}} import {{cookiecutter.model_name|title}}


class {{cookiecutter.model_name|title}}ModelTestCase(TenantTestCase):
    def test_{{cookiecutter.model_name}}_creation(self):
        {{cookiecutter.model_name}} = {{cookiecutter.model_name|title}}.objects.create(first_name="John", last_name="Doe")
        self.assertEqual({{cookiecutter.model_name}}.first_name, "John")
        self.assertEqual({{cookiecutter.model_name}}.last_name, "Doe")


class {{cookiecutter.model_name|title}}APITestCase(TenantTestCase):
    def setUp(self):
        self.{{cookiecutter.model_name}}_data = {
            "first_name": "Alice",
            "last_name": "Johnson",
            "email": "alice@gmail.com",
        }
        self.client = Client(headers={"X-TENANT-ID": super().get_test_schema_name()})

    def test_create_{{cookiecutter.model_name}}(self):
        url = reverse("{{cookiecutter.model_name_plural}}")
        response = self.client.post(url, self.{{cookiecutter.model_name}}_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual({{cookiecutter.model_name|title}}.objects.count(), 1)

    def test_list_{{cookiecutter.model_name_plural}}(self):
        {{cookiecutter.model_name|title}}.objects.create(first_name="Bobby", last_name="Smith")
        url = reverse("{{cookiecutter.model_name_plural}}")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assuming you have more than one {{cookiecutter.model_name}} in the database
        self.assertGreater(len(response.data), 0)

    def test_retrieve_{{cookiecutter.model_name}}(self):
        {{cookiecutter.model_name}} = {{cookiecutter.model_name|title}}.objects.create(first_name="Bob", last_name="Smith")
        url = reverse("{{cookiecutter.model_name}}", args=[{{cookiecutter.model_name}}.id])  # Replace with the correct URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data["response"]["data"]
        self.assertEqual(response_data["first_name"], "Bob")

    def test_update_{{cookiecutter.model_name}}(self):
        {{cookiecutter.model_name}} = {{cookiecutter.model_name|title}}.objects.create(
            first_name="Charlie", last_name="Brown", email="charlie@gmail.com"
        )
        url = reverse("{{cookiecutter.model_name}}", args=[{{cookiecutter.model_name}}.id])
        updated_data = {"first_name": "David", "last_name": "Smith", "email": "david@gmail.com"}
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual({{cookiecutter.model_name|title}}.objects.get(id={{cookiecutter.model_name}}.id).first_name, "David")

    def test_delete_{{cookiecutter.model_name}}(self):
        {{cookiecutter.model_name}} = {{cookiecutter.model_name|title}}.objects.create(first_name="Eve", last_name="Johnson")
        url = reverse("{{cookiecutter.model_name}}", args=[{{cookiecutter.model_name}}.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual({{cookiecutter.model_name|title}}.objects.filter(id={{cookiecutter.model_name}}.id).count(), 0)
