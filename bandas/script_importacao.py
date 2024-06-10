
from bandas.models import Banda
from bandas.models import Album
from bandas.models import Musica
import json

Banda.objects.all().delete()
Album.objects.all().delete()
Musica.objects.all().delete()

with open("bandas/bandas_rock.json") as f:
    bandas = json.load(f)

    for banda in bandas:
        Banda.objects.create(
            nome = banda['nome'],
            anoCriacao = banda['anoCriacao'],
            descricao = banda['descricao']
            )


with open("bandas/discos_rock.json") as f:
    discos = json.load(f)

    for disco in discos:
        Album.objects.create(
            nome = disco['nome'],
            anoLancamento = disco['anoLancamento'],
            banda = Banda.objects.get(nome = disco['autor']),
        )
        for musica in disco['musicas']:
            Musica.objects.create(
                nome = musica['nome'],
                duracao = musica['duracao'],
                album = Album.objects.get(nome = disco['nome']),
            )
