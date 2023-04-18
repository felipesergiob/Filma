from django.urls import path
from django.views.generic import RedirectView
from galeria.views import index, imagem, login, cadastro, post, submit_login, perfil, lista, darlike

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:movie_id>', imagem, name='imagem'),
    path('login/',  login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('post/', post, name='post'),
    path('login/submit', submit_login),
    path('perfil/', perfil, name='perfil'),
    path('lista/', lista, name='lista'),
    path('post/like/<int:pk>/', darlike, name='darlike'),
]