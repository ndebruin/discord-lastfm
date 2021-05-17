#!/usr/bin/python

from os import getenv
from requests import get
from json import loads as json_loads

from dotenv import load_dotenv
load_dotenv()

def lastfm_get():
    headers = {
        'user-agent': 'currently_playing_viewer'
    }

    payload = {
        'api_key': str(getenv("KEY")),
        'method': 'user.getrecenttracks',
        'user': str(getenv("LASTFM_USER")),
        'nowplaying': 'true',
        'limit': '1',
        'format': 'json'
    }

    response = get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
    return response

def format_lastfm():
    names_dict = json_loads(open('names-dict.txt', 'r').read())

    response = dict(lastfm_get().json())
        #is there a better way to do this than this mess below? probably, but this works
    recent_tracks = response["recenttracks"]
    tracks = recent_tracks["track"]
    nowplaying = tracks[0]
    album = nowplaying["album"]
    album_name = album["#text"]
    title = nowplaying["name"]
    if album_name == "":
        album_name = "Cupcake Landers"

    print("{}({}) - {}".format(album_name, names_dict[album_name], title))
    return album_name, names_dict[album_name], title

format_lastfm()