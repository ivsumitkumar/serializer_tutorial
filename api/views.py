from api.models import Singer, Song
from api.serializers import SingerSerializer, SongSerializer
from rest_framework import viewsets


class SingerAPI(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongAPI(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
