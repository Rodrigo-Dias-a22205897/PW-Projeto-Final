from django.shortcuts import render
from .models import Logo

def index_view(request):
    objeto = Logo.objects.get(nome="Logo 1")
    return render(request, "login/index.html", {'objeto': objeto})

def login_view(request):
    objeto = Logo.objects.get(nome="Logo 1")
    return render(request, "login/login.html", {'objeto': objeto})

def register_view(request):
    objeto = Logo.objects.get(nome="Logo 1")
    return render(request, "login/register.html", {'objeto': objeto})

def recover_view(request):
    objeto = Logo.objects.get(nome="Logo 1")
    return render(request, "login/recover.html", {'objeto': objeto})

def logo_view(request):
    objeto = Logo.objects.get(nome="Logo 1")
    return render(request, 'login/index.html', {'objeto': objeto})