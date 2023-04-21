# Generated by Django 4.2 on 2023-04-07 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musiclabapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='music',
            name='genero',
            field=models.CharField(choices=[('axe', 'Axé'), ('blues', 'Blues'), ('country', 'Country'), ('eletronica', 'Eletrônica'), ('forro', 'Forró'), ('funk', 'Funk'), ('gospel', 'Gospel'), ('hip_hop', 'Hip Hop'), ('jazz', 'Jazz'), ('mpb', 'MPB'), ('musica_classica', 'Música Clássica'), ('pagode', 'Pagode'), ('pop', 'Pop'), ('rap', 'Rap'), ('reggae', 'Reggae'), ('rock', 'Rock'), ('samba', 'Samba')], default='rock', max_length=20),
        ),
        migrations.AddField(
            model_name='music',
            name='responsavel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
