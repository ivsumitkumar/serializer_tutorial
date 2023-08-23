from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import  StudentDeserializer,StudentSerializer
from rest_framework.renderers import JSONRenderer 
import io #used in DeSerializer
from rest_framework.parsers import JSONParser #used in deserializer
from django.views.decorators.csrf import csrf_exempt #to bypass csrf

# Create your views here.
# Model Object - single student data
def student_detail(request,x):
    stu = Student.objects.get(id=x)
    stu_serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(stu_serializer.data)
    return HttpResponse(
        json_data,content_type='application/json'
        )

def all_student(request):
    stu = Student.objects.all()
    stu_serializer = StudentSerializer(stu,many = True)
    # json_data = JSONRenderer().render(stu_serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(
        stu_serializer.data,safe=False
        )

@csrf_exempt
def Student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        native_data = JSONParser().parse(stream)
        deserializer = StudentDeserializer(data=native_data)
        if deserializer.is_valid():
            deserializer.save()
            res  = {"msg":"Data inserted!"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
            # return JsonResponse(res_serializer.data,safe=True)
        json_data=JSONRenderer().render(deserializer.errors)
        return HttpResponse(json_data,content_type='application/json')
        # return JsonResponse(deserializer.data,safe=False)