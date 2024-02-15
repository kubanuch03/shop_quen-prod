from rest_framework.permissions import BasePermission

class IsCreatorOrAdmin(BasePermission):
    """
    Разрешает доступ только создателю или администратору.
    """
    def has_object_permission(self, request, view, obj):

        if request.user.is_staff:
            return True

        return obj.created_by == request.user