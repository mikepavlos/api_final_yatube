from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = 'У вас недостаточно прав для выполнения данного действия.'

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )
