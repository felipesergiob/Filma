from django.contrib import admin
from galeria.models import Perfil
from galeria.models import Filme
from galeria.models import Comment

class Perfils(admin.ModelAdmin):
    list_display = ('id', 'nome')
admin.site.register(Perfil, Perfils)

class ListandoFilme(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'genero', 'views_count')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'genero', 'status',)
    list_filter = ('status', 'views_count',)

class ArticleAdmin(admin.ModelAdmin):
    list_select_related = ("status",)

admin.site.register(Filme, ListandoFilme)
admin.site.register(Comment)
