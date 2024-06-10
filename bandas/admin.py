from django.contrib import admin
from .models import Banda
from .models import Album
from .models import Musica
from .models import Logo

class BandaAdmin(admin.ModelAdmin):
    list_display = ('nome','anoCriacao')
    ordering = ('nome','anoCriacao')
    search_fields = ('nome','anoCriacao')

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nome','capa','banda','anoLancamento')
    ordering = ('nome','banda','anoLancamento')
    search_fields = ('nome','banda')

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('nome','duracao','link','hit_da_semana','album')
    ordering = ('nome','album')
    search_fields = ('nome','album')

class LogoAdmin(admin.ModelAdmin):
    list_display = ('nome','link','imagem')
    ordering = ('nome',)
    search_fields = ('nome',)

admin.site.register(Logo, LogoAdmin)
admin.site.register(Banda, BandaAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Musica, MusicaAdmin)