# Generated by Django 4.2 on 2023-05-10 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0017_avaliacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='estrelas',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
