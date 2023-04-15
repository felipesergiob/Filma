from django.contrib import admin
from galeria.models import Perfil

class Perfils(admin.ModelAdmin):
    list_display = ('id', 'nome')

admin.site.register(Perfil, Perfils)