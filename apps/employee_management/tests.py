from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.employee_management.models import Department, Employee


class EmployeeModelTestCase(TestCase):
    def test_employee_creation(self):
        department = Department.objects.create(name="HR")
        employee = Employee.objects.create(first_name="John", last_name="Doe", department=department)
        self.assertEqual(employee.first_name, "John")
        self.assertEqual(employee.last_name, "Doe")


class EmployeeAPITestCase(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(name="IT")
        self.employee_data = {
            "first_name": "Alice",
            "last_name": "Johnson",
            "email": "alice@gmail.com",
            "department_id": self.department.id,
        }
        # self.employee = Employee.objects.create(**self.employee_data)

    def test_create_employee(self):
        url = reverse("employees")
        response = self.client.post(url, self.employee_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)

    def test_list_employees(self):
        Employee.objects.create(first_name="Bobby", last_name="Smith", department=self.department)
        url = reverse("employees")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assuming you have more than one employee in the database
        self.assertGreater(len(response.data), 0)

    def test_retrieve_employee(self):
        employee = Employee.objects.create(first_name="Bob", last_name="Smith", department=self.department)
        url = reverse("employee", args=[employee.id])  # Replace with the correct URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "Bob")

    def test_update_employee(self):
        employee = Employee.objects.create(
            first_name="Charlie", last_name="Brown", email="charlie@gmail.com", department=self.department
        )
        url = reverse("employee", args=[employee.id])
        updated_data = {"first_name": "David", "last_name": "Smith", "email": "david@gmail.com"}
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.get(id=employee.id).first_name, "David")

    def test_delete_employee(self):
        employee = Employee.objects.create(first_name="Eve", last_name="Johnson", department=self.department)
        url = reverse("employee", args=[employee.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.filter(id=employee.id).count(), 0)
