from rest_framework.permissions import BasePermission


# The list only works if is logged in
# the others methods can only be call if the user is staff
class ListDefaultPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user
        return request.user and request.user.is_staff
