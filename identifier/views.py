from identifier.models import Musics
from django.http import HttpResponse
from googleapiclient.discovery import build
import json

# REST
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import Http404

# SOM
from io import BytesIO
import requests


@api_view(['POST'])
def api_identifier(request):

    Musics.objects.all().delete()
    audio_query = request.data['audio-file']
    audio_blob = BytesIO(audio_query.read())

    json_response = find_music(audio_blob)['result']
    s = json.dumps(json_response)
    q = json.dumps(json.loads(s), indent=2)
    #print(q)


    artist = json_response['artist']
    title = json_response['title']
    album = json_response['album']
    release_date = json_response['release_date']

    try:
        genre = json_response['apple_music']['genreNames'][0]
    except:
        genre = " "


    album_picture = json_response['spotify']['album']['images'][0]['url']

    try:
        spotify_link = json_response['spotify']['external_urls']['spotify']
    except:
        spotify_link = " "

    try:
        apple_music_link = json_response['apple_music']['url']
    except:
        apple_music_link = " "

    try:
        deezer_link = json_response['deezer']['link']
    except:
        deezer_link = " "
    
    try:
        napster_link = json_response['napster']['href']
    except:
        napster_link = " "
    
    try:
        lyrics = json_response['lyrics']['lyrics']
    except:
        lyrics = " "
    

    music = Musics(artist=artist, title=title, album=album, release_date=release_date, genre=genre,
    album_picture=album_picture, spotify_link=spotify_link, apple_music_link=apple_music_link,
    deezer_link=deezer_link, napster_link=napster_link, lyrics=lyrics)

    music.save()

    print('\n\n')
    print(f"Id: {music.id}")

    return Response(music.id)

    #return Response("")


def find_music(file):
    data = {
        'api_token': '328103c4a4afbc58d5001326e9ff66bf',
        'return': 'apple_music,spotify,deezer,napster,lyrics',
    }
    files = {
        'file': file,
    }
    result = requests.post('https://api.audd.io/', data=data, files=files)
    
    return result.json()


def index(request):
    return render(request, 'identifier/index.html')


def music(request, id):
    music = Musics.objects.get(id=id)

    logos = ['identifier/img/apple-music-logo.png', 'identifier/img/spotify-logo.png',
             'identifier/img/deezer-logo.png','identifier/img/napster-logo.png']

    links = [music.apple_music_link, music.spotify_link, music.deezer_link, music.napster_link]
    data = {}
    for i in range(len(logos)):
        data[logos[i]] = links[i]

    api_key = "AIzaSyBgjxsWxVrSLlq5ED02fV8k6jXNO3WVAc0"
    youtube = build('youtube', 'v3', developerKey=api_key)
    req = youtube.search().list(q=f"{music.title} {music.artist}", part='snippet', type='video')
    video_id = req.execute()['items'][0]["id"]["videoId"]
    print(video_id)

    src = f"https://www.youtube.com/embed/{video_id}"

    return render(request, 'identifier/music.html', {'data': data, 'music': music, 'src':src})
