from django.contrib import admin
from galeria.models import Perfil
from galeria.models import Filme

class Perfils(admin.ModelAdmin):
    list_display = ('id', 'nome')
admin.site.register(Perfil, Perfils)

class ListandoFilme(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'genero', 'views_count')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'genero',)
admin.site.register(Filme, ListandoFilme)