from rest_framework import viewsets
from ..models import Tutor,Pet
from .serializers import TutorSerializer,PetSerializer
class TutorViewSet(viewsets.ModelViewSet):
    queryset=Tutor.objects.all()
    serializer_class=TutorSerializer
class PetViewSet(viewsets.ModelViewSet):
    queryset=Pet.objects.all()
    serializer_class=PetSerializer