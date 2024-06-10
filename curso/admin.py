from django.contrib import admin
from .models import Curso, LinguagemProgramacao, Docente, AreaCientifica, Disciplina, Projeto, CursoDisciplina

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome','duracao','vagas','creditos','codigo','grau','localizacao')
    ordering = ('nome','grau','localizacao')
    search_fields = ('nome','grau')

class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome','apelido')
    ordering = ('nome',)
    search_fields = ('nome',)

class LinguagemProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

class AreaCientificaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome','ano','semestre','ects','areaCientifica')
    ordering = ('nome','ano','areaCientifica')
    search_fields = ('nome',)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome','disciplina','linguagemProgramacao')
    ordering = ('nome','linguagemProgramacao')
    search_fields = ('nome','linguagemProgramacao')
    
class CursoDisciplinaAdmin(admin.ModelAdmin):
    list_display = ('curso','disciplina')
    ordering = ('curso','disciplina')
    search_fields = ('curso','disciplina')


admin.site.register(Curso, CursoAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(LinguagemProgramacao, LinguagemProgramacaoAdmin)
admin.site.register(AreaCientifica, AreaCientificaAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(CursoDisciplina,CursoDisciplinaAdmin)
