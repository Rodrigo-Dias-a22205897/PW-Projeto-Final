from django.urls import path
from . import views

app_name = 'praias'

urlpatterns = [
    path('', views.index_view, name='praias'),
    path('praia/<str:nome>', views.praia_view, name='praia'),
]