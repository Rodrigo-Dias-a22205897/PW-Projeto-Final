from django.shortcuts import render
from .models import Artigo, Comentario, Rating, Resposta, Utilizador

def artigos_view(request):
    artigos = Artigo.objects.all().order_by('-data')
    return render(request, "artigos/artigos.html", {
        'artigos' : artigos
        })

def artigosTema_view(request,tema):
    tema_numero = None

    for item in Artigo.RATING_CHOICES:
        if item[1] == tema:
            tema_numero  = item[0]
            break

    artigos = Artigo.objects.filter(tema=tema_numero).order_by('-data')

    return render(request, "artigos/artigos.html", {
        'artigos' : artigos
        })

def artigo_view(request, id):
    artigo = Artigo.objects.get(id=id)
    return render(request, "artigos/artigo.html", {
        'artigo' : artigo
        })

def autor_view(request, nome):
    autor = Utilizador.objects.get(nome=nome)
    return render(request, "artigos/autor.html", {
        'autor' : autor
        })