from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешает только владельцу объекта редактировать или удалять его.
    Чтение (GET) доступно всем.
    """
    def has_object_permission(self, request, view, obj):
        # GET, HEAD и OPTIONS разрешены всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Только владелец объекта имеет право на изменение
        return obj.author == request.user
