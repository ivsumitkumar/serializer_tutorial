from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from api.myPagination import myPaginations  # local pagination


#   for global settings of pagination check settings.py file

class StudentAPI(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = myPaginations    # local pagination

