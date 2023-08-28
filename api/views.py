from .models import Student
from .serializers import StudentDeserializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentDeserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]