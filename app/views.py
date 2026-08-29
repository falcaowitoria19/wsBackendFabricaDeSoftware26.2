# Create your views here.
from django.shortcuts import render,get_object_or_404
from.models import Pet

def home(request):
    return render(request, 'pets/home.html')

def cadastrar_tutor(request):
    return render (request,'pets/cadastrar_tutor.html')
def cadastrar_pet(request,tutor_id):
    return render( request,'pets/cadastrar_pet.html',{'tutor_id': tutor_id})
def informacoes_pet(request,id):
    pet=get_object_or_404(Pet,id=id)
    return render(request,'pets/informacoes_pet.html',{'pet':pet})