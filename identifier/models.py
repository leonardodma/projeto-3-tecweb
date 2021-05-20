from os import name
from django.db import models

# Create your models here.
class Musics(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    album_picture = models.CharField(max_length=200)
    spotify_link = models.CharField(max_length=200)
    apple_music_link = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}({self.artist})'
