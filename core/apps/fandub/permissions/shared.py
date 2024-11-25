from rest_framework import permissions


class CommentPermission(permissions.BasePermission):
    def __init__(self) -> None: ...

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request, view):
        return True

    def has_object_permission(
        self, request, view, obj
    ) -> bool:
        if request.method == permissions.SAFE_METHODS:
            return True

        return request.user == obj.user
