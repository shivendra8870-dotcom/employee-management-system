from rest_framework import filters, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Employee
from .permissions import IsAdminOrReadOnlyEmployee
from .serializers import EmployeeSerializer, EmployeeCreateSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.select_related("user").all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["full_name", "email", "employee_id", "department", "job_title"]
    ordering_fields = ["full_name", "date_joined", "created_at"]
    permission_classes = [IsAdminOrReadOnlyEmployee]

    def get_serializer_class(self):
        return EmployeeCreateSerializer if self.request.method == "POST" else EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.select_related("user").all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrReadOnlyEmployee]

    def perform_destroy(self, instance):
        # Deleting the profile also deletes its linked login account.
        instance.user.delete()
