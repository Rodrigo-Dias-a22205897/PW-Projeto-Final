from django.db import models

class Utilizador(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    idade = models.IntegerField()
    foto = models.ImageField(null = True, blank = True)
    data = models.DateTimeField(auto_now = True, auto_now_add = False)

    def __str__(self):
        return f'{self.nome} {self.apelido}'

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    autor = models.ForeignKey(Utilizador, on_delete=models.CASCADE, related_name='artigos')
    foto = models.ImageField(null = True, blank = True)
    data = models.DateTimeField(auto_now = True)

    JURIDICO = 1
    CULTURA = 2
    SAUDE = 3
    DESPORTO = 4
    POLITICA = 5
    GERAL = 6

    RATING_CHOICES = [
        (JURIDICO,'Justiça'),
        (SAUDE,'Saúde'),
        (DESPORTO,'Desporto'),
        (POLITICA,'Política'),
        (CULTURA,'Cultura'),
        (GERAL,'Notícias do Mundo')
    ]

    tema = models.IntegerField(
        choices=RATING_CHOICES, default = 6, blank=True,null=True
    )

    def get_tema(self):
        return dict(self.RATING_CHOICES).get(self.tema)

    def __str__(self):
        return f'{self.titulo}'

class Comentario(models.Model):
    texto = models.TextField()
    autor = models.ForeignKey(Utilizador, on_delete=models.CASCADE, related_name='comentarios')
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return f'{self.texto}'

class Rating(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='ratings')

    MUITO_MAU = 1
    MAU = 2
    MEDIO = 3
    BOM = 4
    MUITO_BOM = 5
    RATING_CHOICES = [
        (MUITO_MAU,'Muito Mau'),
        (MAU,'Mau'),
        (MEDIO,'Médio'),
        (BOM,'Bom'),
        (MUITO_BOM,'Muito Bom'),
    ]

    pontuacao = models.IntegerField(
        choices=RATING_CHOICES, default = 1, blank=True,null=True
    )

    def __str__(self):
        return f'{self.pontuacao}'

class Resposta(models.Model):
    texto = models.TextField()
    autor = models.ForeignKey(Utilizador, on_delete=models.CASCADE, related_name='respostas')
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='respostas', null=True, blank=True)
    resposta = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='respostas')

    def __str__(self):
        if self.comentario:
            return f'Resposta ao Comentário: {self.comentario.texto}'
        elif self.resposta:
            return f'Resposta a {self.resposta}'
