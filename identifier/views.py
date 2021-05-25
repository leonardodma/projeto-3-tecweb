from identifier.models import Musics
from django.http import HttpResponse
import json

# REST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import Http404

# SOM
from io import BytesIO
import requests


@api_view(['GET', 'POST'])
def api_identifier(request):
    """
    if request.method == 'POST':
        Musics.objects.all().delete()
        audio_query = request.data['audio-file']
        audio_blob = BytesIO(audio_query.read())

        response_json = find_music(audio_blob)['result']
        s = json.dumps(response_json)
        q = json.dumps(json.loads(s), indent=2)
        print(q)

        artist = response_json['artist']
        title = response_json['title']
        album = response_json['album']
        release_date = response_json['release_date']
        genre = response_json['apple_music']['genreNames'][0]
        album_picture = response_json['spotify']['album']['images'][0]['url']
        spotify_link = response_json['spotify']['external_urls']['spotify']
        apple_music_link = response_json['apple_music']['url']

        Musics(artist=artist, title=title, album=album, release_date=release_date, genre=genre,
        album_picture=album_picture, spotify_link=spotify_link, apple_music_link=apple_music_link).save()
    """
    return Response("")


def find_music(file):
    data = {
        'api_token': '328103c4a4afbc58d5001326e9ff66bf',
        'return': 'lyrics,apple_music,spotify,deezer',
    }
    files = {
        'file': file,
    }
    result = requests.post('https://api.audd.io/', data=data, files=files)
    
    return result.json()


def index(request):
    return render(request, 'identifier/index.html')


def music(request):
    logos = ['identifier/img/apple-music-logo.png', 'identifier/img/spotify-logo.png',
             'identifier/img/deezer-logo.png','identifier/img/youtube-music-logo.png']
    links = ["", "", "", ""]

    data = {}
    for i in range(len(logos)):
        data[logos[i]] = links[i]


    return render(request, 'identifier/music.html', {'data': data})