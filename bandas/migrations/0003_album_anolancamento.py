# Generated by Django 4.0.6 on 2024-04-04 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0002_album_capa_musica_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='anoLancamento',
            field=models.IntegerField(default=3000),
        ),
    ]
