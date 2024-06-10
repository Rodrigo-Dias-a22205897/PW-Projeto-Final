from django.urls import path
from . import views

app_name = 'novaapp'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('calculator/', views.calculator_view, name='calculator'),
    path('contact/', views.contact_view, name='contact'),
]