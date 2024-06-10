from django.contrib import admin
from django.utils.html import format_html
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome','apelido','idade')
    ordering = ('nome','idade')
    search_fields = ('nome','apelido')

admin.site.register(Pessoa, PessoaAdmin)
