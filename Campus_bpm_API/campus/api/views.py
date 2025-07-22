from rest_framework.viewsets import ModelViewSet
from campus.models import Musicas, Bpm
from campus.api.serializers import MusicaSerilizer, BpmSerilizer

class MusicaViewSet(ModelViewSet):
    queryset = Musicas.objects.all()
    serializer_class = MusicaSerilizer

class BpmViewSet(ModelViewSet):
    queryset = Bpm.objects.all()
    serializer_class = BpmSerilizer