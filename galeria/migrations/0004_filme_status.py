# Generated by Django 4.2 on 2023-04-16 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_filme'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='status',
            field=models.CharField(choices=[('WATCHLIST', 'Watchlist'), ('ASSISTIDO', 'Assistido'), ('FAVORITO', 'Favorito')], max_length=100),
        ),
    ]
