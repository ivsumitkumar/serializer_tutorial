from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
# from rest_framework.authentication import BasicAuthentication  # Locally
# from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser    # Locally

#for globally check settings.py file

class StudentAPI(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]    # Locally
    # permission_classes = [IsAuthenticated]    # Locally
    # permission_classes = [AllowAny]   # this api can be accessed by anyone without authentication
    # permission_classes = [IsAdminUser]   # this api can be accessed by staff only
    
    
