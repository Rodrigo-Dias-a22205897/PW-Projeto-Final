from django.shortcuts import render,redirect
from .models import Logo, Album, Banda, Musica
from django.contrib.auth import authenticate, login, models, logout
from django.contrib.auth.models import Group
from .forms import AlbumForm, BandaForm, MusicaForm


def index_view(request):
    logos = Logo.objects.exclude(nome='Home')
    return render(request, "bandas/index.html", {'logos': logos})

def bandas_view(request):
    home = Logo.objects.get(nome='Home')
    bandas = Banda.objects.exclude(nome='Spotily')
    return render(request, "bandas/bandas.html", {
        'home': home,
        'bandas' : bandas
        })

def edit_bandas_view(request):
    user = request.user
    is_member = user.groups.filter(name='bandas').exists()

    if(is_member):
        home = Logo.objects.get(nome='Home')
        bandas = Banda.objects.exclude(nome='Spotily')
        return render(request, "bandas/edit_bandas.html", {
            'home': home,
            'bandas' : bandas
            })
    else:
        return redirect('bandas:index')

def albuns_view(request):
    home = Logo.objects.get(nome='Home')
    albuns = Album.objects.exclude(nome='Hits da Semana')
    return render(request, "bandas/albuns.html", {
        'home': home,
        'albuns': albuns
        })

def edit_albuns_view(request):
    user = request.user
    is_member = user.groups.filter(name='bandas').exists()

    if(is_member):
        home = Logo.objects.get(nome='Home')
        albuns = Album.objects.exclude(nome='Hits da Semana')
        return render(request, "bandas/edit_albuns.html", {
            'home': home,
            'albuns': albuns
            })
    else:
        return redirect('bandas:index')

def hits_view(request):
    home = Logo.objects.get(nome='Home')
    hits = Musica.objects.filter(hit_da_semana=True)
    return render(request, "bandas/hits.html", {
        'home': home,
        'hits': hits
        })

def album_view(request,nome):
    home = Logo.objects.get(nome='Home')
    album = Album.objects.get(nome=nome)
    return render(request, "bandas/album.html", {
        'home': home,
        'album': album
        })

def banda_view(request,nome):
    home = Logo.objects.get(nome='Home')
    banda = Banda.objects.get(nome=nome)
    return render(request, "bandas/banda.html", {
        'home': home,
        'banda': banda
        })

def musica_view(request,nome):
    home = Logo.objects.get(nome='Home')
    musica = Musica.objects.get(nome=nome)
    return render(request, "bandas/musica.html", {
        'home': home,
        'musica': musica
        })

def edit_musicas_view(request):
    user = request.user
    is_member = user.groups.filter(name='bandas').exists()

    if(is_member):
        home = Logo.objects.get(nome='Home')
        musicas = Musica.objects.all()
        return render(request, "bandas/edit_musicas.html", {
            'home': home,
            'musicas': musicas
            })
    else:
        return redirect('bandas:index')


def user_view(request):
    home = Logo.objects.get(nome='Home')
    user = request.user
    is_member = user.groups.filter(name='bandas').exists()

    context = {
        'is_member': is_member,
        'home': home,
    }
    return render(request, "bandas/user.html", context)

def login_view(request):
    home = Logo.objects.get(nome='Home')
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('bandas:user')
        else:
            render(request, 'bandas/login.html', {
                'mensagem':'Credenciais inválidas',
                'home': home
            })

    return render(request, 'bandas/login.html',{
                'home': home
            })

def register_view(request):
    home = Logo.objects.get(nome='Home')
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('bandas:login')

    return render(request, 'bandas/register.html',{
                'home': home
            })

def logout_view(request):
    logout(request)
    return redirect('bandas:index')

def novo_album_view(request):
    user = request.user
    is_member = user.groups.filter(name='bandas').exists()

    if(is_member):
        home = Logo.objects.get(nome='Home')
        form = AlbumForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bandas:edit_albuns')

        context = {
            'form': form,
            'home': home,
        }
        return render(request, 'bandas/novo_album.html', context)
    else:
        return redirect('bandas:index')


def apaga_album_view(request, album_nome):
    user = request.user
    is_member = user.groups.filter(name='bandas').exists()

    if(is_member):
        album = Album.objects.get(nome=album_nome)
        album.delete()
        return redirect('bandas:edit_albuns')
    else:
        return redirect('bandas:index')

def novo_banda_view(request):
    user = request.user
    is_member = user.groups.filter(name='bandas').exists()

    if(is_member):
        home = Logo.objects.get(nome='Home')
        form = BandaForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bandas:edit_bandas')

        context = {
            'form': form,
            'home': home,
        }
        return render(request, 'bandas/novo_banda.html', context)
    else:
        return redirect('bandas:index')

def apaga_banda_view(request, banda_nome):
    user = request.user
    is_member = user.groups.filter(name='bandas').exists()

    if(is_member):
        banda = Banda.objects.get(nome=banda_nome)
        banda.delete()
        return redirect('bandas:edit_bandas')
    else:
        return redirect('bandas:index')

def novo_musica_view(request):
    user = request.user
    is_member = user.groups.filter(name='bandas').exists()

    if(is_member):
        home = Logo.objects.get(nome='Home')
        form = MusicaForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bandas:edit_musicas')

        context = {
            'form': form,
            'home': home,
        }
        return render(request, 'bandas/novo_musica.html', context)
    else:
        return redirect('bandas:index')

def apaga_musica_view(request, musica_nome):
    user = request.user
    is_member = user.groups.filter(name='bandas').exists()

    if(is_member):
        musica = Musica.objects.get(nome=musica_nome)
        musica.delete()
        return redirect('bandas:edit_musicas')
    else:
        return redirect('bandas:index')

def edita_album_view(request, album_id):
    user = request.user
    is_member = user.groups.filter(name='bandas').exists()

    if(is_member):
        album = Album.objects.get(id=album_id)

        if request.POST:
            form = AlbumForm(request.POST or None, request.FILES, instance=album)
            if form.is_valid():
                form.save()
                return redirect('bandas:edit_albuns')
        else:
            form = AlbumForm(instance=album)

        context = {'form': form, 'album':album}
        return render(request, 'bandas/edita_album.html', context)
    else:
        return redirect('bandas:index')

def edita_musica_view(request, musica_id):
    user = request.user
    is_member = user.groups.filter(name='bandas').exists()

    if(is_member):
        musica = Musica.objects.get(id=musica_id)

        if request.POST:
            form = AlbumForm(request.POST or None, request.FILES, instance=musica)
            if form.is_valid():
                form.save()
                return redirect('bandas:edit_musicas')
        else:
            form = MusicaForm(instance=musica)

        context = {'form': form, 'musica':musica}
        return render(request, 'bandas/edita_musica.html', context)
    else:
        return redirect('bandas:index')

def edita_banda_view(request, banda_id):
    user = request.user
    is_member = user.groups.filter(name='bandas').exists()

    if(is_member):
        banda = Banda.objects.get(id=banda_id)

        if request.POST:
            form = BandaForm(request.POST or None, request.FILES, instance=banda)
            if form.is_valid():
                form.save()
                return redirect('bandas:edit_bandas')
        else:
            form = BandaForm(instance=banda)

        context = {'form': form, 'banda':banda}
        return render(request, 'bandas/edita_banda.html', context)
    else:
        return redirect('bandas:index')