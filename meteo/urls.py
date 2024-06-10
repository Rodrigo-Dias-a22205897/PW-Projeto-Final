from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('previsao/<int:globalIdLocal>', views.previsao_view, name='previsao'),
    path('api/', views.api_view, name='api'),
    path('cidades/', views.cidades_view, name='get_cidades'),
    path('previsao/hoje/<int:globalIdLocal>', views.api_previsao_hoje_view, name='get_previsao_1'),
    path('previsao/semana/<int:globalIdLocal>', views.api_previsao_semana_view, name='get_previsao_2'),
    path('previsao/img/', views.api_img_view, name='get_img'),
]