from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .viewsets import TutorViewSet,PetViewSet

router=DefaultRouter()

router.register("tutores",TutorViewSet)
router.register("pets",PetViewSet)
urlpatterns =router.urls