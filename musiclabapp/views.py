from django.shortcuts import render, redirect
from .models import Music, Album, Playlist
import pygame
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from .forms import AlbumForm, MusicForm, PlaylistForm
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

@login_required(login_url='/auth/logar/')
def home_music(request):
    genero = request.GET.get('genero', '')
    musics = Music.objects.all()

    if genero:
        musics = musics.filter(genero=genero)

    return render(request, 'home_music.html', {'musics': musics})





@login_required(login_url='/auth/logar/')
def select_music(request):
    return render(request, 'select_music.html')

@login_required(login_url='/auth/logar/')
def stop_music(request):
    return render(request, 'stop_music.html')


@login_required(login_url='/auth/logar/')
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})



@login_required(login_url='/auth/logar/')
def music_list(request):
    musics = Music.objects.all()
    return render(request, 'music_list.html', {'musics': musics})



@login_required(login_url='/auth/logar/')
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)
            album.title = album.album
            album.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'add_album.html', {'form': form})



@login_required(login_url='/auth/logar/')
def add_music(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            album_id = request.POST.get('album')
            for file in request.FILES.getlist('file'):
                music = Music()
                music.album = Album.objects.get(pk=album_id)
                music.file = file
                music.title = file.name
                music.genero = request.POST.get('genero')
                music.artist = request.POST.get('artist')
                music.responsavel = request.user
                music.save()
            return redirect('music_list')
    else:
        form = MusicForm()
    return render(request, 'add_music.html', {'form': form})






@login_required(login_url='/auth/logar/')
def create_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data.get('nome')
            musicas = form.cleaned_data.get('musicas')
            playlist = Playlist.objects.create(nome=nome)
            playlist.musicas.set(musicas)
            return redirect('playlist_list')
    else:
        form = PlaylistForm()
    
    # Seleciona todas as músicas e as agrupa por artista e gênero
    musicas = Music.objects.all().order_by('artist', 'genero')
    musicas_agrupadas = {}
    for musica in musicas:
        if musica.artist not in musicas_agrupadas:
            musicas_agrupadas[musica.artist] = {}
        if musica.genero not in musicas_agrupadas[musica.artist]:
            musicas_agrupadas[musica.artist][musica.genero] = []
        musicas_agrupadas[musica.artist][musica.genero].append(musica)

    return render(request, 'create_playlist.html', {'form': form, 'musicas_agrupadas': musicas_agrupadas})


@login_required(login_url='/auth/logar/')
def playlist_list(request):
    playlists = Playlist.objects.all()
    context = {'playlists': playlists}
    return render(request, 'playlist_list.html', context)



@login_required(login_url='/auth/logar/')
def add_music_to_playlist(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    if request.method == 'POST':
        music_ids = request.POST.getlist('music')
        musics = Music.objects.filter(id__in=music_ids)
        playlist.musicas.add(*musics)
        messages.success(request, 'Músicas adicionadas com sucesso à playlist.')
        return redirect('playlist_detail', playlist_id=playlist.id)
    else:
        musicas = Music.objects.all()
        context = {
            'playlist': playlist,
            'musicas': musicas,
        }
        return render(request, 'add_music_to_playlist.html', context)



@login_required(login_url='/auth/logar/')
def search_music(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            results = Music.objects.filter(Q(title__icontains=query) | Q(album__title__icontains=query) | Q(artist__icontains=query))
            return render(request, 'search_music.html', {'results': results, 'query': query})
    return redirect('home_music')



@login_required(login_url='/auth/logar/')
def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    musics = Music.objects.filter(album=album)
    return render(request, 'album_detail.html', {'album': album, 'musics': musics})


@login_required(login_url='/auth/logar/')
def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'edit_album.html', {'form': form, 'album': album})



@login_required(login_url='/auth/logar/')
def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        messages.success(request, 'Álbum excluído com sucesso!')
        return redirect('album_list')
    return render(request, 'delete_album.html', {'album': album})



@login_required(login_url='/auth/logar/')
def delete_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = get_object_or_404(Music, pk=song_id)
    song.delete()
    return redirect('edit_album', album_id=album.id)



@login_required(login_url='/auth/logar/')
def add_song(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.album = album
            song.save()
            return redirect('edit_album', album_id=album.id)
    else:
        form = MusicForm()
    return render(request, 'add_song.html', {'album': album, 'form': form})



