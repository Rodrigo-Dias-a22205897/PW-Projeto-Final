from django.db import models

# Create your models here.

class Regiao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'

class Praia(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='praias/fotos', null = True, blank = True)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE, related_name='praias')

    def __str__(self):
        return f'{self.nome}'

class Servico(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'

class PraiaServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='lista')
    praia = models.ForeignKey(Praia, on_delete=models.CASCADE, related_name='lista')

    def __str__(self):
        return f'{self.servico} - {self.praia}'