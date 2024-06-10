from django.db import models

# Create your models here.

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome} {self.apelido}'

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()
    duracao = models.CharField(max_length=100)
    vagas = models.IntegerField(default=0)
    creditos = models.IntegerField()
    codigo = models.IntegerField()

    LICENCIATURA = 1
    MESTRADO = 2
    MESTRADO_INTEGRADO = 3
    DOUTURAMENTO = 4
    POS_GRADUACAO = 5
    RATING_CHOICES = [
        (LICENCIATURA,'Licenciatura'),
        (MESTRADO,'Mestrado'),
        (MESTRADO_INTEGRADO,'Mestrado Integrado'),
        (DOUTURAMENTO,'Douturamento'),
        (POS_GRADUACAO,'Pos-Graduação'),
    ]

    grau = models.IntegerField(
        choices=RATING_CHOICES, default = 1, blank=True,null=True
    )

    LISBOA = 1
    PORTO = 2
    RATING_CHOICES_2 = [
        (LICENCIATURA,'Centro Universitário Lisboa'),
        (MESTRADO,'Centro Universitário Porto'),
    ]

    localizacao = models.IntegerField(
        choices=RATING_CHOICES_2, default = 1, blank=True,null=True
    )

    def __str__(self):
        return f'{self.nome}'

class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'

class AreaCientifica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=100)
    ects = models.IntegerField()
    curricularIUnitReadableCode = models.CharField(max_length=100)
    areaCientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE, related_name='disciplinas')
    docentes = models.ManyToManyField(Docente,related_name='disciplinas')

    def __str__(self):
        return f'{self.nome}'

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    conceitos = models.TextField()
    tecnologias = models.TextField()
    imagem = models.ImageField(upload_to='curso/fotos', null = True, blank = True)
    linkGit = models.URLField(max_length=200,default='/default-url/')
    linkVideo = models.URLField(max_length=200,default='/default-url/')
    disciplina = models.OneToOneField(Disciplina,on_delete=models.CASCADE,related_name='projeto')
    linguagemProgramacao = models.ForeignKey(LinguagemProgramacao, on_delete=models.CASCADE, related_name='projetos')

    def __str__(self):
        return f'{self.nome}'

class CursoDisciplina(models.Model):
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, related_name='lista')
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, related_name='lista')

    def __str__(self):
        return f'{self.curso} - {self.disciplina}'

