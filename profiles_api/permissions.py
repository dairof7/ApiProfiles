from rest_framework import permissions

class UpdatePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj.id)
        print(request.user)
        return obj.id == request.user.id