# Generated by Django 4.0.6 on 2024-04-15 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0009_alter_logo_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logo',
            name='path',
        ),
    ]
