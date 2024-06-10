from .models import Curso, CursoDisciplina, Projeto, Disciplina, Docente
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, models, logout
from django.contrib.auth.models import Group
from curso.forms import ProjetoForm, CursoForm, DisciplinaForm, DocenteForm

def index_view(request):
    cursos = Curso.objects.all()
    return render(request, "curso/index.html", {
        'cursos' : cursos
        })

def curso_view(request,curso):
    curso = Curso.objects.get(nome=curso)

    return render(request, "curso/curso.html", {
        'curso' : curso
        })

def disciplina_view(request,curso,disciplina):
    disciplina = CursoDisciplina.objects.get(disciplina__nome=disciplina,curso__nome=curso)

    return render(request, "curso/disciplina.html", {
        'disciplina' : disciplina
        })

def projeto_view(request,disciplina,projeto):
    projeto = Projeto.objects.get(nome=projeto)

    return render(request, "curso/projeto.html", {
        'projeto' : projeto
        })

def user_view(request):
    user = request.user
    is_member = user.groups.filter(name='curso').exists()

    context = {
        'is_member': is_member,
    }
    return render(request, "curso/user.html", context)

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('curso:user')
        else:
            render(request, 'curso/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'curso/login.html')

def register_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('curso:login')

    return render(request, 'curso/register.html')

def logout_view(request):
    logout(request)
    return redirect('curso:universidade')

def edit_cursos_view(request):
    cursos = Curso.objects.all()
    return render(request, "curso/edit_cursos.html", {
        'cursos' : cursos
        })

def edit_disciplinas_view(request):
    disciplinas = Disciplina.objects.all()
    return render(request, "curso/edit_disciplinas.html", {
        'disciplinas' : disciplinas
        })

def edit_projetos_view(request):
    projetos = Projeto.objects.all()
    return render(request, "curso/edit_projetos.html", {
        'projetos' : projetos
        })

def edit_docentes_view(request):
    docentes = Docente.objects.all()
    return render(request, "curso/edit_docentes.html", {
        'docentes' : docentes
        })

def apaga_curso_view(request, curso_nome):
    curso = Curso.objects.get(nome=curso_nome)
    curso.delete()
    return redirect('bandas:edit_cursos')

def novo_curso_view(request):
    form = CursoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:edit_cursos')

    context = {'form': form}
    return render(request, 'curso/novo_curso.html', context)

def apaga_disciplina_view(request, disciplina_nome):
    disciplina = Disciplina.objects.get(nome=disciplina_nome)
    disciplina.delete()
    return redirect('bandas:edit_disciplinas')

def novo_disciplina_view(request):
    form = DisciplinaForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:edit_disciplinas')


    context = {'form': form}
    return render(request, 'curso/novo_disciplina.html', context)

def apaga_docente_view(request, docente_nome):
    docente = Docente.objects.get(nome=docente_nome)
    docente.delete()
    return redirect('bandas:edit_docentes')

def novo_docente_view(request):
    form = DocenteForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:edit_docentes')


    context = {'form': form}
    return render(request, 'curso/novo_docente.html', context)

def apaga_projeto_view(request, projeto_nome):
    projeto = Projeto.objects.get(nome=projeto_nome)
    projeto.delete()
    return redirect('bandas:edit_docentes')

def novo_projeto_view(request):
    form =ProjetoForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('bandas:edit_projetos')


    context = {'form': form}
    return render(request, 'curso/novo_projeto.html', context)