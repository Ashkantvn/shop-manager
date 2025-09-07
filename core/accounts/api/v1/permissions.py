from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    """
    Custom permission to only allow managers to access certain views.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and is a manager
        return (
            hasattr(request.user, "business_manager")
            and request.user.business_manager is not None
        )

    def has_object_permission(self, request, view, obj):
        # Optionally, you can add object-level permission checks here
        return self.has_permission(request, view)
