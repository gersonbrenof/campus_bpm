from rest_framework import serializers
from campus.models import Bpm, Musicas

class MusicaSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Musicas
        fields = ['id', 'link']
        
        
class BpmSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Bpm
        fields= ['id', 'notificacao', 'historico']
        
    
        
        