from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome = models.CharField(max_length=70, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
#Adicionando filmes ao banco de dados
class Filme(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    genero = models.CharField(max_length=100, null=False, blank=False)
    elenco = models.CharField(max_length=100)
    sinopse = models.TextField(max_length=1000)
    capa = models.CharField(max_length=100, null=False, blank=False)
    ano_de_producao = models.DateField()
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo