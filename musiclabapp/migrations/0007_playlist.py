# Generated by Django 4.2 on 2023-04-08 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiclabapp', '0006_album_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('musicas', models.ManyToManyField(to='musiclabapp.music')),
            ],
        ),
    ]
