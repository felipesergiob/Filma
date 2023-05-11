from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    nome = models.CharField(max_length=70, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


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
    estrelas = models.FloatField(default=0, blank=True)

    def __str__(self):
        return self.titulo
    
    def total_favs(self):
        return self.favourites.count()
    
    def total_wl(self):
        return self.watchlists.count()

    def calcular_media_estrelas(self):
        total_avaliacoes = self.avaliacoes.count()
        if total_avaliacoes > 0:
            media_estrelas = self.avaliacoes.aggregate(media=Avg('estrelas'))['media']
            return media_estrelas
        return 0.0

    def save(self, *args, **kwargs):
        self.estrelas = self.calcular_media_estrelas()
        super().save(*args, **kwargs)

class Avaliacao(models.Model):
    filme = models.ForeignKey(Filme, related_name='avaliacoes', on_delete=models.CASCADE)
    estrelas = models.IntegerField()
    
class Comment(models.Model):
    filme = models.ForeignKey(Filme, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def total_comments(self):
        return self.filme.comments.count()
    
