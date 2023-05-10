from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome = models.CharField(max_length=70, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
#Adicionando filmes ao banco de dados
class Filme(models.Model):

    OPCOES_STATUS = [
        ("WATCHLIST", "Watchlist"),
        ("ASSISTIDO", "Assistido"),
        ("FAVORITO", "Favorito"),
    ]

    titulo = models.CharField(max_length=100, null=False, blank=False)
    genero = models.CharField(max_length=100, null=False, blank=False)
    status = models.CharField(max_length=100, choices=OPCOES_STATUS, blank=True)
    elenco = models.CharField(max_length=100)
    sinopse = models.TextField(max_length=1000)
    capa = models.ImageField(upload_to="capas_movie", blank=False)
    ano_de_producao = models.DateField()
    views_count = models.IntegerField(default=0)
    favourites = models.ManyToManyField(User, related_name='favourites', blank=True)
    watchlists = models.ManyToManyField(User, related_name='watchlists', blank=True)

    def __str__(self):
        return self.titulo
    
    def total_favs(self):
        return self.favourites.count()
    
    def total_wl(self):
        return self.watchlists.count()
