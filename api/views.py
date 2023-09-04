from django.shortcuts import render
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# from rest_framework.throttling import ScopedRateThrottle


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)
