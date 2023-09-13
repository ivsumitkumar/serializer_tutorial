from rest_framework import serializers
from api.models import Singer, Song


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender']


class SongSerializer(serializers.ModelSerializer):
    sungby = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='singer-detail')

    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration', 'sungby']
