
from .models import Curso, AreaCientifica, Disciplina, CursoDisciplina
import json

with open("curso/ficheiro") as f:
    info = json.load(f)

    curso = Curso.objects.create(
        codigo = info['courseDetail']['courseCode'],
        nome = info['courseDetail']['courseName'],
        competencias = info['courseDetail']['competences'],
        duracao = info['hrContactoSoma'],
        creditos = info['courseDetail']['courseECTS'],
    )

    area = AreaCientifica.objects.create(
        nome = info['courseDetail']['scientificArea']
    )

    for disciplina_info in info['courseFlatPlan']:
        disciplina = Disciplina.objects.create(
            curricularIUnitReadableCode = disciplina_info['curricularIUnitReadableCode'],
            nome = disciplina_info['curricularUnitName'],
            ano = disciplina_info['curricularYear'],
            ects = disciplina_info['ects'],
            semestre = disciplina_info['semester'],
            areaCientifica= area,
        )
        relacao = CursoDisciplina.objects.create(
            curso = curso,
            disciplina = disciplina,
        )
