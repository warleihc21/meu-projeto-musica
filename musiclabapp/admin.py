from django.contrib import admin
from musiclabapp.models import *
from .models import Album, Music



admin.site.register(Album)
admin.site.register(Music)


