# Generated by Django 3.2 on 2021-04-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExhibitionsWebApp', '0002_artwork_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitionhall',
            name='exhibitions',
            field=models.ManyToManyField(default=int, to='ExhibitionsWebApp.Exhibition'),
        ),
    ]