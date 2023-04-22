from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home_music/', views.home_music, name='home_music'),
    path('select_music/', views.select_music, name='select_music'),
    path('stop_music/', views.stop_music, name='stop_music'),
    path('albums/', views.album_list, name='album_list'),
    path('add_album/', views.add_album, name='add_album'),
    path('musics/', views.music_list, name='music_list'),
    path('add_music/', views.add_music, name='add_music'),
    path('create_playlist/', views.create_playlist, name='create_playlist'),
    path('playlist_list/', views.playlist_list, name='playlist_list'),
    path('minha_playlist/', views.minha_playlist, name='minha_playlist'),
    path('add_music_to_playlist/<int:music_id>/', views.add_music_to_playlist, name='add_music_to_playlist'),


    

    path('search_music/', views.search_music, name='search_music'),
    path('album_detail/<int:album_id>/', views.album_detail, name='album_detail'),
    path('albums/<int:album_id>/', views.album_detail, name='album_detail'),
    path('albums/<int:pk>/edit/', views.edit_album, name='edit_album'),
    path('albums/<int:pk>/delete/', views.delete_album, name='delete_album'),
    path('edit_album/', views.edit_album, name='edit_album'),
    path('albums/<int:pk>/add_song/', views.add_song, name='add_song'),
    path('albums/<int:pk>/delete_song/<int:song_pk>/', views.delete_song, name='delete_song'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)