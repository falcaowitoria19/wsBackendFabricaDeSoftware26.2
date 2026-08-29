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

