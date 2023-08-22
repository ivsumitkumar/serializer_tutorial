# from django import forms
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

# class StduentForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     roll = forms.IntegerField()
#     city = forms.CharField(max_length=100)