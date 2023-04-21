from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    album = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, blank=False, error_messages={'blank': 'Este campo é obrigatório.'})
    cover_art = models.ImageField(upload_to='cover_art', blank=True, null=True)
    release_date = models.DateField()
    

    def __str__(self):
        return self.album

class Music(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='file')
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    file = models.FileField(upload_to='file')
    genero_choices = (('axe', 'Axé'),
                      ('blues', 'Blues'),
                      ('country', 'Country'),
                      ('eletronica', 'Eletrônica'),
                      ('forro', 'Forró'),
                      ('funk', 'Funk'),
                      ('gospel', 'Gospel'),
                      ('hip_hop', 'Hip Hop'),
                      ('jazz', 'Jazz'),
                      ('mpb', 'MPB'),
                      ('musica_classica', 'Música Clássica'),
                      ('pagode', 'Pagode'),
                      ('pop', 'Pop'),
                      ('rap', 'Rap'),
                      ('reggae', 'Reggae'),
                      ('rock', 'Rock'),
                      ('metal', 'Metal'),
                      ('hardcore', 'Hardcore'),
                      ('punk', 'Punk'),
                      ('samba', 'Samba'))
    genero = models.CharField(choices=genero_choices, max_length=20, blank=True, null=True)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.first().id)

    def __str__(self):
        return self.title
    

class Playlist(models.Model):
    nome = models.CharField(max_length=100)
    musicas = models.ManyToManyField(Music)

    def __str__(self):
        return self.nome
