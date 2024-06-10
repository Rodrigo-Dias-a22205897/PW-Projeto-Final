from django.shortcuts import render
import requests

def index_view(request):
    return render(request, "portefolio/index.html")
