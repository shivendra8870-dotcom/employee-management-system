from datetime import date
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Employee

User = get_user_model()

class EmployeeAPITests(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="TestPass123!"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin)

    def test_admin_can_create_employee(self):
        response = self.client.post("/api/employees/", {
            "username": "jane",
            "password": "StrongPass123!",
            "employee_id": "EMP-001",
            "full_name": "Jane Doe",
            "email": "jane@example.com",
            "department": "Engineering",
            "job_title": "Python Developer",
            "phone": "9000000000",
            "date_joined": "2025-01-15",
            "is_active": True,
        }, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Employee.objects.count(), 1)

    def test_admin_can_list_employees(self):
        user = User.objects.create_user(username="sam", password="TestPass123!")
        Employee.objects.create(
            user=user, employee_id="EMP-002", full_name="Sam Lee",
            email="sam@example.com", department="Finance",
            job_title="Analyst", date_joined=date(2025, 2, 1),
        )
        response = self.client.get("/api/employees/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
