from django import forms
from .models import Album, Music, Playlist
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, DateInput, FileInput, Select
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album', 'title', 'artist', 'cover_art', 'release_date']
        widgets = {
            'album': forms.TextInput(attrs={'class': 'form-control', 'style': "max-width: 300px;",
                'placeholder': "Digite o nome do álbum..."}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': "max-width: 300px;",
                'placeholder': "Digite algum título..."}),
            'artist': forms.TextInput(attrs={'class': 'form-control', 'style': "max-width: 300px;",
                'placeholder': "Digite o nome do artista..."}),
            'cover_art': forms.FileInput(attrs={'class': 'form-control', 'style': "max-width: 300px;",
                'placeholder': "Adicione a imagem...",'type': 'file'}),
            'release_date': forms.DateInput(attrs={'class': 'form-control', 'style': "max-width: 300px;",
                'placeholder': "Selecione a data...", 'type': 'date'}),

        }





class MusicForm(forms.ModelForm):
    title = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'style': "max-width: 300px;"}))
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control', 'style': "max-width: 300px;"}))
    

    class Meta:
        model = Music
        fields = ['album', 'title', 'artist', 'file', 'genero']
        widgets = {
            'album': forms.Select(attrs={'class': 'form-control', 'style': "max-width: 300px;",
                'placeholder': "Digite o nome do álbum..."}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': "max-width: 300px;",
                'placeholder': "Digite algum título..."}),
            'artist': forms.TextInput(attrs={'class': 'form-control', 'style': "max-width: 300px;",
                'placeholder': "Digite o nome do artista..."}),
            'file': forms.FileInput(attrs={'class': 'form-control', 'style': "max-width: 300px;",
                'placeholder': "Adicione a imagem...",'type': 'file'}),
            'genero': forms.Select(attrs={'class': 'form-control', 'style': "max-width: 300px;",
                'placeholder': "Selecione o genero...", 'type': 'select', 'for':"{{ form.genero.id_for_label }}"}),

        }

    def clean(self):
        cleaned_data = super().clean()
        file = cleaned_data.get('file')
        if not cleaned_data.get('title'):
            title = file.name.split('.')[0]
            cleaned_data['title'] = title

        # Obter a instância do álbum selecionado
        album = cleaned_data['album']
        album_instance = Album.objects.get(pk=album.pk)
        cleaned_data['artist'] = album_instance.artist
        return cleaned_data
    


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['nome', 'musicas']
        widgets = {
            'musicas': forms.CheckboxSelectMultiple(),
        }