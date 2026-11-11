from django.conf import settings
from django.db import models

class Employee(models.Model):
    DEPARTMENTS = [
        ("Engineering", "Engineering"),
        ("Human Resources", "Human Resources"),
        ("Finance", "Finance"),
        ("Sales", "Sales"),
        ("Operations", "Operations"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employee_profile",
    )
    employee_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=40, choices=DEPARTMENTS)
    job_title = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    date_joined = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return f"{self.employee_id} - {self.full_name}"
