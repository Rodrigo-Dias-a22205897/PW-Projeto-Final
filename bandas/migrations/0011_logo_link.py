# Generated by Django 4.0.6 on 2024-04-15 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0010_remove_logo_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='link',
            field=models.URLField(default='/default-url/'),
        ),
    ]
