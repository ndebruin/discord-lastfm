#!/usr/bin/python

from os import getenv
from requests import get
from time import sleep

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

response = dict(lastfm_get().json())
#is there a better way to do this than this mess below? probably, but this works
recenttracks = response["recenttracks"]
tracks = recenttracks["track"]
nowplaying = tracks[0]
album = nowplaying["album"]
albumName = album["#text"]
title = nowplaying["name"]
if albumName == "":
    albumName = "Cupcake Landers"

print("{} - {}".format(albumName, title))
