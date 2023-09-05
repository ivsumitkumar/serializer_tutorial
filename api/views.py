from api.models import Student
from api.serializers import StudentSerializer
from rest_framework import viewsets


class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
