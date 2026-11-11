from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnlyEmployee(BasePermission):
    """Admins can manage records; authenticated employees can read them."""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (
            request.method in SAFE_METHODS or request.user.is_staff
        ))
