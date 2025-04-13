from rest_framework import permissions

class IsTenantUser(permissions.BasePermission):
    """
    Permission to only allow users from the current tenant.
    """
    def has_permission(self, request, view):
        return hasattr(request, 'tenant')
