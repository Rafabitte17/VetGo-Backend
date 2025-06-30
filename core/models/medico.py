from django.db import models


class Medico(models.Model):
    nome_completo = models.CharField(max_length=45)
    data_nascimento = models.DateField
    