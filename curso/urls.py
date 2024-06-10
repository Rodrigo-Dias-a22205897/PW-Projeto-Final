from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('', views.index_view, name='universidade'),
    path('<str:curso>', views.curso_view, name='curso'),
    path('<str:curso>/<str:disciplina>', views.disciplina_view, name='disciplina'),
    path('<str:disciplina>/projeto/<str:projeto>', views.projeto_view, name='projeto'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('user/', views.user_view, name='user'),
    path('edit/admin/curso/all', views.edit_cursos_view, name="edit_cursos"),
    path('edit/admin/projeto/all', views.edit_projetos_view, name="edit_projetos"),
    path('edit/admin/docente/all', views.edit_docentes_view, name="edit_docentes"),
    path('edit/admin/disciplina/all', views.edit_disciplinas_view, name="edit_disciplinas"),
    path('curso/<str:curso_nome>/apaga/1', views.apaga_curso_view,name="apaga_curso"),
    path('curso/novo/admin/1', views.novo_curso_view, name="novo_curso"),
    path('disciplina/<str:disciplina_nome>/apaga/1', views.apaga_disciplina_view,name="apaga_disciplina"),
    path('disciplina/novo/admin/1', views.novo_disciplina_view, name="novo_disciplina"),
    path('docente/<str:docente_nome>/apaga/1', views.apaga_docente_view,name="apaga_docente"),
    path('docente/novo/admin/1', views.novo_docente_view, name="novo_docente"),
    path('projeto/<str:projeto_nome>/apaga/1', views.apaga_projeto_view,name="apaga_projeto"),
    path('projeto/novo/admin/1', views.novo_projeto_view, name="novo_projeto"),
]