from django.shortcuts import render
from galeria.forms import GaleriaForms

def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')

def login(request):
    return render(request, 'galeria/login.html')

def cadastro(request):
    return render(request, 'galeria/cadastro.html')

def post(request):
    form = GaleriaForms()
    contexto = {'form':form}
    return render(request, 'galeria/post.html', contexto)
