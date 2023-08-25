from rest_framework import serializers
from .models import Student


# Model Serializer
class StudentDeserializer(serializers.ModelSerializer):
    #validators
    def checkCaps(value):
        if value[0] != value[0].upper():
            raise serializers.ValidationError('First letter must be capital!')
    name = serializers.CharField(validators=[checkCaps]) # adding validators method 1

    class Meta:
        model = Student
        fields = ['name','roll','city']
        # read_only_fields = ['name','roll']    # adding validators method 2
        # extra_kwargs = {'name':{'read_only':True} # adding validators method 3

    # Field level validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError("Seats are full!")
        return value
    
    # Object level Validation
    def validate(self,value):
        nm = value.get('name')
        ct = value.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'kashmir':
            raise serializers.ValidationError('city must be Kashmir!')
        return value



class StudentSerializer(serializers.Serializer):    #used in GET
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
