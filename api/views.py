from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes,authentication_classes # decorators for authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])

#functioned Based API view
def studentapi(request,pk=None):

    if request.method =='GET':
        # id = request.data.get('id')   
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            stu_serializer = StudentSerializer(stu)
            return Response(stu_serializer.data)
        stu = Student.objects.all()
        stu_serializer = StudentSerializer(stu,many=True)
        return Response(stu_serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':
        stu_serializer = StudentSerializer(data=request.data)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(stu_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(id=id)
        stu_serializer = StudentSerializer(stu, data=request.data)

        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response({'msg':'Complete Data Updated!'}, status=status.HTTP_204_NO_CONTENT)
        return Response(stu_serializer.errors)
    
    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(id=pk)
        stu_serializer = StudentSerializer(stu,data=request.data,partial = True)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response({'msg':'Data Updated!'})
        return Response(stu_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data Deleted'},status=status.HTTP_204_NO_CONTENT)
