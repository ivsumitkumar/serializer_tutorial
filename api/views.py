from .models import Student
from .serializers import StudentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            stu_serializer = StudentSerializer(Student.objects.get(id=id))
            return Response(stu_serializer.data, status = status.HTTP_200_OK)
        stu_serializer = StudentSerializer(Student.objects.all(),many=True)
        return Response(stu_serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request,format=None):
        stu_serializer = StudentSerializer(data=request.data)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(stu_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        stu_serializer = StudentSerializer(Student.objects.get(id=pk),data=request.data, partial=False)

        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response({'msg':'Data Updated!'}, status=status.HTTP_204_NO_CONTENT)
        return Response(stu_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk, format=None):
        stu_serializer = StudentSerializer(Student.objects.get(id=pk),data=request.data,partial=True)
        if stu_serializer.is_valid():
            stu_serializer.save()
            return Response({'msg':'Partial Data Updated!'}, status=status.HTTP_204_NO_CONTENT)
        return Response(stu_serializer.errors, status=status.HTTP_204_NO_CONTENT)

    def delete(self,request,pk,format=None):
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg':'Data Deleted!'},status=status.HTTP_204_NO_CONTENT)
        