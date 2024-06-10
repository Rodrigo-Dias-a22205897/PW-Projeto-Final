from django.shortcuts import render

def index_view(request):
    return render(request, "calculadora/index.html")