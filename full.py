#!/usr/bin/python

from pypresence import Presence
from os import getenv
from time import sleep, time
from requests import get
from json import loads as json_loads
from dotenv import load_dotenv

#load env variables from .env file
load_dotenv()

#otherwise python gets mad
old_title = ""

#connect to discord client
RPC = Presence(getenv("DISCORD"))
RPC.connect()

def lastfm():
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

    names_dict = json_loads(open('names-dict.txt', 'r').read())

    response = dict(response.json())
    nowplaying = response["recenttracks"]["track"][0]
    album_name = nowplaying["album"]["#text"]
    title = nowplaying["name"]
    
    if album_name == "":
        album_name = "Cupcake Landers"

    return album_name, names_dict[album_name], title

#keep program constantly running
while True:
    #get new data from last.fm
    album_name, asset_name, title = lastfm()

    #if track is same as track from previous check, do not update
    if old_title == title:
        continue

    else:
        #update RPC with title of song, start time, and album art + name
        RPC.update(state="Listening to {}".format(title), start=time(), 
        large_image=asset_name, large_text=album_name, 
        small_image='lollypop', small_text="Lollypop Music Player")
        old_title = title

    sleep(15)