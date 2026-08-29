from django.db import models
# Create your models here.
class Tutor(models.Model):
    nome=models.CharField(max_length=50)
    telefone=models.CharField(max_length=20)
    email=models.EmailField()

    def __str__(self):
        return self.nome

class Pet(models.Model):
    nome=models.CharField(max_length=60)
    especie=models.CharField(max_length=50)
    raca=models.CharField(max_length=60)
    idade=models.IntegerField()
    tutor=models.ForeignKey(Tutor,on_delete=models.CASCADE,related_name="pets")
    def __str__(self):
        return self.nome

class Consulta(models.Model):
    pet=models.ForeignKey(Pet,on_delete=models.CASCADE,related_name="consultas")
    data=models.DateField()
    motivo_consulta=models.CharField(max_length=250)
    observacao=models.TextField(blank=True)
    status=models.CharField(max_length=30)
    def __str__(self):
        return f"{self.pet.nome} - {self.data}"