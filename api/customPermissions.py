from rest_framework.permissions import BasePermission, IsAuthenticated

class myPermissions(IsAuthenticated, BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET','HEAD','OPTIONS']:
            return True

        if request.method in ['POST','PUT','DELETE','PATCH'] and IsAuthenticated.has_permission(self,request, view):
            return True
        return False