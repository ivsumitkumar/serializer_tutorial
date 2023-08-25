from rest_framework import serializers
from .models import Student


#validators - high priority
def checkCaps(value):
    if value[0] != value[0].upper():
        raise serializers.ValidationError('First letter must be capital!')

class StudentSerializer(serializers.Serializer):    #used in GET
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100,validators=[checkCaps])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100,validators=[checkCaps])

class StudentDeserializer(serializers.Serializer):  #used in POST
    name = serializers.CharField(max_length=100,validators=[checkCaps])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100,validators=[checkCaps])

    def create(self,validate_data):     #used for POST method
        return Student.objects.create(**validate_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    #field Level Validation - priority is less than validators
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError("Seats are full!")
        return value
    
    # Object level validation - used when validation more than one field, priority is less than field level validators
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'kashmir':
            raise serializers.ValidationError('city must be Kashmir!')
        return data