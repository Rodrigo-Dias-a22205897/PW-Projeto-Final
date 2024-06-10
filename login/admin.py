from django.contrib import admin
from .models import Logo

class LogoAdmin(admin.ModelAdmin):
    list_display = ('nome','imagem')
    ordering = ('nome',)
    search_fields = ('nome',)

admin.site.register(Logo, LogoAdmin)