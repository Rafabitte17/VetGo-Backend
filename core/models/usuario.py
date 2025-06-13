from django.db import models


class Usuario(models.Model):
    nome_completo_usua = models.CharField(max_length=45)
    data_nascimento_usua = models.DateTimeField()
    telefone_usua = models.CharField(max_length=10)
    cpf_usua = models.CharField(max_length=12)
    email_usua = models.CharField(max_length=45)
    Consultas_idConsultas = models.IntegerField()  

    def __str__(self):
        return self.nome_completo_usua
