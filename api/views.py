from .models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response

from django.shortcuts import render

class StudentAPI(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        stu_serializer = StudentSerializer(stu,many = True)
        return Response(stu_serializer.data)
    
    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            stu = Student.objects.get(id=id)
            stu_serializer = StudentSerializer(stu)
            return Response(stu_serializer.data)
        
    def create(self,request):
        stu_serailizer = StudentSerializer(data = request.data)
        if stu_serailizer.is_valid():
            stu_serailizer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(stu_serailizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        id = pk
        stu = Student.objects.get(id=id)
        stu_serializer = StudentSerializer(stu, data=request.data)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response({'msg':'Data Updated'},status=status.HTTP_202_ACCEPTED)
        return Response(stu_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        id = pk
        stu = Student.objects.get(id=id)
        stu_serializer = StudentSerializer(stu, data=request.data, partial=True)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response({'msg':'Data Updated'},status=status.HTTP_202_ACCEPTED)
        return Response(stu_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted!'},status=status.HTTP_202_ACCEPTED)
    
