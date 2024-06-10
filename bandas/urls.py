from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('bandas/', views.bandas_view, name='bandas'),
    path('albuns/', views.albuns_view, name='albuns'),
    path('hits/', views.hits_view, name='hits'),
    path('album/<str:nome>/', views.album_view, name='album'),
    path('banda/<str:nome>/', views.banda_view, name='banda'),
    path('musica/<str:nome>/', views.musica_view, name='musica'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name="logout"),
    path('user/', views.user_view, name="user"),
    path('album/novo', views.novo_album_view, name="novo_album"),
    path('edit/albuns', views.edit_albuns_view, name="edit_albuns"),
    path('album/<str:album_nome>/apaga', views.apaga_album_view,name="apaga_album"),
    path('banda/novo', views.novo_banda_view, name="novo_banda"),
    path('edit/bandas', views.edit_bandas_view, name="edit_bandas"),
    path('banda/<str:banda_nome>/apaga', views.apaga_banda_view,name="apaga_banda"),
    path('musica/novo', views.novo_musica_view, name="novo_musica"),
    path('edit/musicas', views.edit_musicas_view, name="edit_musicas"),
    path('musica/<str:musica_nome>/apaga', views.apaga_musica_view,name="apaga_musica"),
    path('album/<int:album_id>/edita', views.edita_album_view,name="edita_album"),
    path('musica/<int:musica_id>/edita', views.edita_musica_view,name="edita_musica"),
    path('banda/<int:banda_id>/edita', views.edita_banda_view,name="edita_banda"),
]