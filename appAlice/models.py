from django.db import models

# Create your models here.

class Adotar(models.Model):
  opcoes1 = [
    ("S", "Sempre"),
    ("N", "Nunca"),
    ("A", "As vezes"), 
  ]
  titulo = models.CharField(max_length=50)
  motivo = models.CharField(max_length=50)
  nivelAgitado = models.CharField(max_length=1, choices = opcoes1)
  expecVida = models.CharField(max_length=20)

class TerAnimais(models.Model):
  titulo = models.CharField(max_length=50)
  resumo = models.CharField(max_length=80)
  genero = models.CharField(max_length=50)
  dataLancamento = models.DateField()
 