from rest_framework import serializers
from campus.models import Registro, Musicas

class MusicaSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Musicas
        fields = ['id', 'link']
        
        
class BpmSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields= ['id', 'data', 'hora']
        
    
        
        