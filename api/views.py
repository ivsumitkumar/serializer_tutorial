from .models import Student
from .serializers import StudentSerializer

from rest_framework.generics import ListAPIView

class StudentAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
