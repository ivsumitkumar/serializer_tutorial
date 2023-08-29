from .models import Student
from .serializers import StudentSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class StudentAPI(ListCreateAPIView):
    queryset = Student.objects.all()    # use .all() or .get_queryset()
    serializer_class = StudentSerializer

class RUDStudentAPI(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.get_queryset()
    serializer_class = StudentSerializer

