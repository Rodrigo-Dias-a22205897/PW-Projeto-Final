from django.shortcuts import render

def index_view(request):
    return render(request, "novaapp/index.html")

def about_view(request):
    return render(request, "novaapp/about.html")

def calculator_view(request):
    return render(request, "novaapp/calculator.html")

def contact_view(request):
    return render(request, "novaapp/contact.html")