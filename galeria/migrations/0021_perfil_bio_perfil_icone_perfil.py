# Generated by Django 4.2 on 2023-06-12 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0020_alter_avaliacao_filme'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='icone_perfil',
            field=models.ImageField(default='default.jpg', upload_to='icone_perfil'),
        ),
    ]
