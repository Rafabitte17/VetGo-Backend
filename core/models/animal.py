from django.db import models


class Animal(models.Model):
    nome_animal = models.CharField(max_length=45)
    raça_animal = models.CharField(max_length=35)
    especie_animal = models.CharField(max_length=35)
    idade_animal = models.BigIntegerField
