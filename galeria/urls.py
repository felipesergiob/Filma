from django.urls import path
from galeria.views import index, imagem, login, cadastro, post, submit_login, perfil, lista

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:movie_id>', imagem, name='imagem'),
    path('login/',  login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('post/', post, name='post'),
    path('login/login.html', submit_login),
    path('perfil/', perfil, name='perfil'),
    path('lista/', lista, name='lista'),
]