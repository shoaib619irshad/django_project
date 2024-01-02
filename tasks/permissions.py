from rest_framework.permissions import BasePermission
from django.http import Http404

from user.models import CustomUser

SAFE_METHODS = ['GET', 'PATCH', 'HEAD', 'OPTIONS']

class IsAdmin(BasePermission):
   
    def has_permission(self, request, view):
        try:
            role = request.user.role
        except Exception:
            raise Http404()
        is_true = (role == CustomUser.ADMIN)
        return bool(is_true and request.user.is_authenticated)
    
class IsManager(BasePermission):
   
    def has_permission(self, request, view):
        try:
            role = request.user.role
        except Exception:
            raise Http404()
        is_true = (role == CustomUser.MANAGER)
        return bool(request.method in SAFE_METHODS and is_true and request.user.is_authenticated)
    
class IsEmployee(BasePermission):
   
    def has_permission(self, request, view):
        try:
            role = request.user.role
        except Exception:
            raise Http404()
        is_true = (role == CustomUser.EMPLOYEE)
        return bool(request.method in SAFE_METHODS and is_true and request.user.is_authenticated)