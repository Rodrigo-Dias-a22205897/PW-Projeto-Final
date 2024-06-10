from django.contrib import admin
from .models import Regiao, Praia, Servico, PraiaServico

class RegiaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

class PraiaAdmin(admin.ModelAdmin):
    list_display = ('nome','foto','regiao')
    ordering = ('nome','regiao')
    search_fields = ('nome','regiao')

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

class PraiaServicoAdmin(admin.ModelAdmin):
    list_display = ('servico','praia')
    ordering = ('servico','praia')
    search_fields = ('servico','praia')


admin.site.register(Regiao, RegiaoAdmin)
admin.site.register(Praia, PraiaAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(PraiaServico, PraiaServicoAdmin)
