# Generated by Django 4.0.6 on 2024-04-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0011_logo_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='descricao',
            field=models.TextField(default=''),
        ),
    ]
