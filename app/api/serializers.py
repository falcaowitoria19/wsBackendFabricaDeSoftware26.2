from rest_framework import serializers
from ..models import Tutor,Pet
class TutorSerializer(serializers.ModelSerializer):
    class Meta:
      model= Tutor
      fields=['id','nome','telefone','email']
        
class PetSerializer(serializers.ModelSerializer):
    class Meta:
      model=Pet
      fields=['id','nome','especie','raca','idade','tutor']
        