# Generated by Django 4.0.6 on 2024-04-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0004_alter_album_anolancamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='capa',
            field=models.ImageField(blank=True, null=True, upload_to='bandas/fotos'),
        ),
    ]
