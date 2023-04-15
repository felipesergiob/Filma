from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Perfil(models.Model):
    nome = models.CharField(max_length=70, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

#Adicionando filmes ao banco de dados  
class Filme2(models.Model):
    Titulo = models.CharField(max_length=100, null=False, blank=False)
    Genero = models.CharField(max_length=100, null=False, blank=False)
    Elenco = models.CharField(max_length=500)
    Sinopse = models.TextField(max_length=1000)
    Avaliacao = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    Capa = models.CharField(max_length=100, null=False, blank=False)
    Ano_de_producao = models.DateField()
    Status = models.CharField(max_length=100)
    Views_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Filme [Titulo={self.Titulo}]"