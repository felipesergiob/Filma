from django.urls import path
from django.views.generic import RedirectView
from galeria.views import index, imagem, login, cadastro, submit_login, perfil, lista, buscar, favViews, watchlist

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:movie_id>', imagem, name='imagem'),
    path('login/',  login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/submit', submit_login),
    path('perfil/', perfil, name='perfil'),
    path('lista/', lista, name='lista'),
    path("buscar", buscar, name="buscar"),
    path('fav/<int:pk>/', favViews, name='favViews'),
    path('watchlist/<int:pk>/', watchlist, name='watchlist'),
]