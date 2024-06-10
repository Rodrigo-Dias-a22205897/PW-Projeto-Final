from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('recover/', views.recover_view, name='recover'),
]