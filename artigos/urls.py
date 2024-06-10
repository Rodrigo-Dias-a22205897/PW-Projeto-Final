from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.artigos_view, name='artigos'),
    path('artigo/<int:id>', views.artigo_view, name='artigo'),
    path('autor/<str:nome>', views.autor_view, name='autor'),
    path('<str:tema>', views.artigosTema_view, name='artigos_tema'),
]