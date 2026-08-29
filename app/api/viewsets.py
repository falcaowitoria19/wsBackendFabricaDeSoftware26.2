import requests
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Tutor,Pet
from .serializers import TutorSerializer,PetSerializer
class TutorViewSet(viewsets.ModelViewSet):
    queryset=Tutor.objects.all()
    serializer_class=TutorSerializer
class PetViewSet(viewsets.ModelViewSet):
    queryset=Pet.objects.all()
    serializer_class=PetSerializer
    @action(detail=True, methods=['GET'])
    def raca(self, request, pk=None):

        pet = self.get_object()

        raca = pet.raca.lower().strip().replace(" ", "-")

        url = f"https://dog.ceo/api/breed/{raca}/images/random"

        try:

            resposta = requests.get(url, timeout=5)

            if resposta.status_code == 200:

                dados = resposta.json()

                return Response({
                    "pet": pet.nome,
                    "raca": pet.raca,
                    "imagem": dados["message"]
                })

            return Response(
                {
                    "erro": "Não foi possível encontrar imagens dessa raça."
                },
                status=resposta.status_code
            )

        except requests.RequestException:

            return Response(
                {
                    "erro": "Não foi possível consultar a API externa."
                },
                status=503
            )