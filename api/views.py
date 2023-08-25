from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import  StudentDeserializer,StudentSerializer
from rest_framework.renderers import JSONRenderer 
import io #used in DeSerializer
from rest_framework.parsers import JSONParser #used in deserializer
from django.views.decorators.csrf import csrf_exempt #to bypass csrf in function based views

from django.utils.decorators import method_decorator    # used to bypass csrf in class based view
from django.views import View   #used in class based view

# Create your views here.

# class based view
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self,request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        native_data = JSONParser().parse(stream)
        id = native_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            stu_serializer = StudentSerializer(stu)
            return JsonResponse(stu_serializer.data,safe=False)
        stu = Student.objects.all()
        stu_serializer = StudentSerializer(stu,many=True)
        return JsonResponse(stu_serializer.data,safe=False)
    
    def post(self,request, *args, **kwargs):
        json_data = request.body            # takes json data
        stream = io.BytesIO(json_data)      # Make stream of json data i.e parsing json data
        native_data = JSONParser().parse(stream)    #parsing of data to native datatype
        deserializer = StudentDeserializer(data=native_data) #converting native to complex type or model instances
        if deserializer.is_valid():         # validating data
            deserializer.save()             # saving data
            res  = {"msg":"Data inserted!"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data=JSONRenderer().render(deserializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    def put(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        native_data = JSONParser().parse(stream)
        id=native_data.get('id')
        stu = Student.objects.get(id=id)
        stu_serializer = StudentDeserializer(stu,data=native_data,partial=True)
        if stu_serializer.is_valid():
            stu_serializer.save()
            res={"msg":"Data Updated"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(stu_serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def delete(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        native_data = JSONParser().parse(stream)
        id = native_data.get('id')

        stu = Student.objects.get(id=id)
        stu.delete()
        res={'msg':'Entry Deleted!'}
        return JsonResponse(res,safe=False)
