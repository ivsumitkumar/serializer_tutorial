# Docs Link:- https://docs.google.com/document/d/1Vcti2pt4ll-Kvb5SpCKHSQZYZw4CWNVat0y3pLqmPWM/edit?usp=sharing


from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .customPermissions import myPermissions


class StudentAPI(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [myPermissions]

    
    
