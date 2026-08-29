"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app.views import home,cadastrar_tutor,cadastrar_pet,informacoes_pet
from drf_spectacular.views import (SpectacularAPIView,SpectacularSwaggerView,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('api/',include('app.api.urls')),
    path('api/schema/',SpectacularAPIView.as_view(), name="schema"),
    path('api/docs/',SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui'),
    path('cadastrar_tutor/',cadastrar_tutor,name='cadastrar_tutor'),
    path('cadastrar_pet/<int:tutor_id>/',cadastrar_pet,name='cadastrar_pet'),
    path('informacoes_pet/<int:id>/',informacoes_pet,name='informacoes_pet'),
]
