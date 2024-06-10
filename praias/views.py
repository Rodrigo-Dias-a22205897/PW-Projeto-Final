from django.shortcuts import render
from .models import Regiao, Praia

# Create your views here.

def index_view(request):
    regioes = Regiao.objects.all()
    return render(request, "praias/index.html", {
        'regioes' : regioes
        })

def praia_view(request, nome):
    praia = Praia.objects.get(nome=nome)
    return render(request, "praias/praia.html", {
        'praia' : praia
        })
