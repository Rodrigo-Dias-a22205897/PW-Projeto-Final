from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    anoCriacao = models.IntegerField()
    descricao = models.TextField(default='')
    nacionalidade = models.CharField(max_length=100, default='')
    foto = models.ImageField(upload_to='bandas/fotos', null = True, blank = True)

    def __str__(self):
        return f'{self.nome}'

class Album(models.Model):
    nome = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='bandas/fotos', null = True, blank = True)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='albuns')
    anoLancamento = models.IntegerField()

    def __str__(self):
        return f'{self.nome} - {self.banda}'

class Musica(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.FloatField()
    descricao = models.TextField(default='')
    link = models.URLField(max_length=200,default='/default-url/')
    hit_da_semana = models.BooleanField(default=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musicas')
    letra = models.TextField(default='')

    def __str__(self):
        return f'{self.nome} - {self.duracao} minutos'

class Logo(models.Model):
    nome = models.CharField(max_length=100)
    link = models.URLField(max_length=200,default='/default-url/')
    imagem = models.ImageField(upload_to='login/fotos', null = True, blank = True)

    def __str__(self):
        return f'{self.nome}'
