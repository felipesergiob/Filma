from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from galeria.forms import Perfilform,GaleriaForms
from django.contrib.auth.forms import UserCreationForm
from galeria.models import Filme


#@login_required(login_url='login')
def index(request):
    filmes = Filme.objects.all()
    return render(request, 'galeria/index.html', {"cards": filmes})

def imagem(request):
    return render(request, 'galeria/imagem.html')

def login(request):
    return render(request, 'galeria/login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(username=username, password=password)

        if usuario:
            return redirect('index')
        else:
            messages.error(request, "Usuário ou senha inválido")
            return redirect('login')

def cadastro(request):
    form = Perfilform(request.POST)

    if request.method =="POST":
        form = Perfilform(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            return redirect('login')
    return render(request, 'galeria/cadastro.html', {'form':form})  

def post(request):
    form = GaleriaForms()
    contexto = {'form':form}
    return render(request, 'galeria/post.html', contexto)
