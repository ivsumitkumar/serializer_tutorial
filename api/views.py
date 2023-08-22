from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
# Model Object - single student data
def student_detail(request,x):
    stu = Student.objects.get(id=x)
    stu_serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(stu_serializer.data)
    return HttpResponse(json_data,content_type='application/json')

def all_student(request):
    stu = Student.objects.all()
    stu_serializer = StudentSerializer(stu,many = True)
    # json_data = JSONRenderer().render(stu_serializer.data)
    # return HttpResponse(json_data,content_type='application/json')

    return JsonResponse(stu_serializer.data,safe=False)
