from django.forms import ModelForm
from .models import Tutor,Pet,Consulta

class TutorForm(ModelForm):
   class Meta:
      model= Tutor
      fields=['nome','telefone','email']

class PetForm(ModelForm):
   class Meta:
      model=Pet
      fields=['nome','especie','raca','idade','tutor']

class ConsultaForm(ModelForm):
   class Meta:
    model=Consulta
    fields=['pet','data','motivo_consulta','observacao','status']