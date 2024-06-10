from django import forms
from .models import Projeto, Curso, Disciplina, Docente

class ProjetoForm(forms.ModelForm):
  class Meta:
    model = Projeto
    fields = '__all__'

class CursoForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields = '__all__'

class DisciplinaForm(forms.ModelForm):
  class Meta:
    model = Disciplina
    fields = '__all__'

class DocenteForm(forms.ModelForm):
  class Meta:
    model = Docente
    fields = '__all__'