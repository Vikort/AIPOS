# Generated by Django 3.2 on 2021-04-19 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExhibitionsWebApp', '0004_alter_exhibitionhall_exhibitions'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='artists/'),
        ),
        migrations.AddField(
            model_name='artwork',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='artworks/'),
        ),
        migrations.AddField(
            model_name='exhibition',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='exhibitions/'),
        ),
        migrations.AddField(
            model_name='exhibitionhall',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='exhibitionHalls/'),
        ),
        migrations.AddField(
            model_name='owner',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='owners/'),
        ),
    ]
