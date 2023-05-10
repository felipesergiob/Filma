from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.models import User
from django.contrib import messages
from galeria.forms import Perfilform,GaleriaForms
from galeria.models import Filme, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView

#@login_required(login_url='login')
def index(request):
    filmes = Filme.objects.order_by("-views_count").all()
    return render(request, 'galeria/index.html', {"cards": filmes})

def imagem(request, movie_id):

    filme = get_object_or_404(Filme, pk=movie_id)
    tem_fav = request.user in filme.favourites.all()
    tem_wl = request.user in filme.watchlists.all()

    context = {
        'filme': filme,
        'favs': filme.total_favs(),
        'wls': filme.total_wl(),
        'tem_fav': tem_fav,
        'tem_wl': tem_wl,
        }
    return render(request, 'galeria/imagem.html', context)

def buscar(request):
    filmes = Filme.objects.order_by("-views_count").all()

    if "buscar" in request.GET:
        titulo_a_buscar = request.GET['buscar']
        if titulo_a_buscar:
            filmes = filmes.filter(titulo__icontains=titulo_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": filmes})

def login(request):
    return render(request, 'galeria/login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login_user(request, usuario)
            return redirect('/')
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

def lista(request):
    return render(request, 'galeria/lista.html')

login_required(login_url='login')
def perfil(request):
    return render(request, 'galeria/perfil.html')

def favViews(request, pk):
    url = request.META.get('HTTP_REFERER')
    filme = get_object_or_404(Filme, id=pk)
    if request.user in filme.favourites.all():
        filme.favourites.remove(request.user)
    else:
        filme.favourites.add(request.user)
    return HttpResponseRedirect(url)

def watchlist(request, pk):
    filme = get_object_or_404(Filme, id=pk)
    if request.user in filme.watchlists.all():
        filme.watchlists.remove(request.user)
    else:
        filme.watchlists.add(request.user)
    return HttpResponseRedirect(reverse('imagem', args=[str(pk)]))

from django.views.generic.edit import CreateView
from galeria.models import Comment

class AddCommentView(CreateView):
    model = Comment
    template_name = 'galeria/add_comentario.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filme'] = get_object_or_404(Filme, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.filme = get_object_or_404(Filme, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('imagem', kwargs={'movie_id': self.kwargs['pk']})
