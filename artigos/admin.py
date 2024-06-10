from django.contrib import admin
from .models import Utilizador
from .models import Artigo
from .models import Comentario
from .models import Rating
from .models import Resposta

class UtilizadorAdmin(admin.ModelAdmin):
    list_display = ('nome','apelido','idade','foto','data')
    ordering = ('nome','idade','data')
    search_fields = ('nome','apelido')

class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo','texto','autor','tema','data')
    ordering = ('autor','data')
    search_fields = ('titulo','autor','data')

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('texto','autor','artigo')
    ordering = ('autor','artigo')
    search_fields = ('autor','artigo')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('artigo','pontuacao')
    ordering = ('artigo','pontuacao')
    search_fields = ('artigo','pontuacao')

class RespostaAdmin(admin.ModelAdmin):
    list_display = ('texto','autor','comentario','resposta')
    ordering = ('autor','comentario')
    search_fields = ('autor','comentario')


admin.site.register(Utilizador, UtilizadorAdmin)
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Resposta, RespostaAdmin)
