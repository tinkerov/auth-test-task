from rest_framework import permissions

class HasRolePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        required_roles = getattr(view, 'required_roles', [])
        if not required_roles:
            return True
            
        user_roles = request.user.roles.values_list('name', flat=True)
        return any(role in user_roles for role in required_roles)