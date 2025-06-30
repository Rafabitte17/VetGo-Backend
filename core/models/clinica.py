from django.db import models


class Clinica(models.Model):
    nome_clinica = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    localizacao = models.CharField(max_length=50)
