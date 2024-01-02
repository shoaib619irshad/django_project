from rest_framework.permissions import BasePermission

from user.models import CustomUser

SAFE_METHODS = ['GET', 'PATCH', 'DELETE']

class IsAdmin(BasePermission):
   
    def has_permission(self, request, view):
        try:
            role = request.user.role
        except AttributeError:
            return False
        is_true = (role == CustomUser.ADMIN)
        return bool(is_true)
    
class IsManager(BasePermission):
   
    def has_permission(self, request, view):
        try:
            role = request.user.role
        except AttributeError:
            return False
        is_true = (role == CustomUser.MANAGER)
        return bool(request.method in SAFE_METHODS and is_true)
    
class IsEmployee(BasePermission):
   
    def has_permission(self, request, view):
        try:
            role = request.user.role
        except AttributeError:
            return False
        is_true = (role == CustomUser.EMPLOYEE)
        return bool(request.method in SAFE_METHODS and is_true)