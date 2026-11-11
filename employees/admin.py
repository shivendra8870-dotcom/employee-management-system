from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "full_name", "email", "department", "job_title", "is_active")
    list_filter = ("department", "is_active")
    search_fields = ("employee_id", "full_name", "email")
