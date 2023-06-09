from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_user, logout
from django.contrib.auth.models import User
from django.contrib import messages
from galeria.forms import Perfilform, CommentForm, AvaliacaoForm
from galeria.models import Filme, Comment, Avaliacao
from django.http import HttpResponseRedirect 
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.db.models import Avg
from django.utils.decorators import method_decorator

#@login_required(login_url='login')
def index(request):
    filmes = Filme.objects.order_by("-views_count").all()
    tem_fav = False
    tem_wl = False

    context = {
        'cards': filmes,
        'favs': 0,
        'wls': 0,
        'tem_fav': tem_fav,
        'tem_wl': tem_wl,
    }

    return render(request, 'galeria/index.html', context)

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

def views(request):
    filmes = Filme.objects.order_by("-views_count").all()

    return render(request, "galeria/views.html", {"cards": filmes})

def buscar(request):
    filmes = Filme.objects.order_by("-views_count").all()

    if "buscar" in request.GET:
        titulo_a_buscar = request.GET['buscar']
        if titulo_a_buscar:
            filmes = filmes.filter(titulo__icontains=titulo_a_buscar)

    return render(request, "galeria/buscar.html", {"cards": filmes})

def login(request):
    return render(request, 'galeria/login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

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

@login_required(login_url='login')
def lista(request):
    favourite_filmes = Filme.objects.filter(favourites=request.user)
    watchlist_filmes = Filme.objects.filter(watchlists=request.user)

    context = {
        'favourite_filmes': favourite_filmes,
        'watchlist_filmes': watchlist_filmes
    }
    
    return render(request, 'galeria/lista.html', context)


@login_required(login_url='login')
def perfil(request):
    return render(request, 'galeria/perfil.html')

@login_required(login_url='login')
def favViews(request, pk):
    url = request.META.get('HTTP_REFERER')
    filme = get_object_or_404(Filme, id=pk)
    if request.user in filme.favourites.all():
        filme.favourites.remove(request.user)
    else:
        filme.favourites.add(request.user)
    return HttpResponseRedirect(url)

@login_required(login_url='login')
def watchlist(request, pk):
    filme = get_object_or_404(Filme, id=pk)
    if request.user in filme.watchlists.all():
        filme.watchlists.remove(request.user)
    else:
        filme.watchlists.add(request.user)
    return HttpResponseRedirect(reverse('imagem', args=[str(pk)]))

@login_required(login_url='login')
def avaliar_filme(request, filme_id):
    filme = get_object_or_404(Filme, pk=filme_id)
    
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        avaliacao = Avaliacao(filme=filme, estrelas=rating)
        avaliacao.save()
        
        media_estrelas = filme.avaliacoes.aggregate(media=Avg('estrelas'))['media']
        filme.estrelas = media_estrelas or 0 
        filme.save()
        
        return HttpResponseRedirect(reverse('imagem', args=[str(filme_id)]))


     
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'galeria/add_comentario.html'
    #fields = '__all__'

    @method_decorator(login_required(login_url='login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filme'] = get_object_or_404(Filme, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.filme = get_object_or_404(Filme, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('imagem', kwargs={'movie_id': self.kwargs['pk']})
   