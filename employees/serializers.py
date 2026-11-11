from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Employee

User = get_user_model()

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id", "employee_id", "full_name", "email", "department",
            "job_title", "phone", "date_joined", "is_active",
            "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

class EmployeeCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = Employee
        fields = [
            "username", "password", "employee_id", "full_name", "email",
            "department", "job_title", "phone", "date_joined", "is_active",
        ]

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def create(self, validated_data):
        username = validated_data.pop("username")
        password = validated_data.pop("password")
        user = User.objects.create_user(username=username, password=password,
                                        email=validated_data["email"])
        return Employee.objects.create(user=user, **validated_data)
