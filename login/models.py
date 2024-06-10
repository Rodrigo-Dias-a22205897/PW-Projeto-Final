from django.db import models

# Create your models here.

class Logo(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='login/fotos', null = True, blank = True)

    def __str__(self):
        return f'{self.nome}'