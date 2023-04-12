from django.urls import path
from galeria.views import index, imagem, login, cadastro, post

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
    path('login/',  login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('post/', post, name='post'),
]