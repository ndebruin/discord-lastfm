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
    
    try: 
        playing_status = response["recenttracks"]["track"][0]['@attr']["nowplaying"]
    except: playing_status = False

    if playing_status == "true":
        playing_status = True

    if album_name == "":
        album_name = "Cupcake Landers"

    return album_name, names_dict[album_name], title, playing_status

#keep program constantly running
while True:
    #get new data from last.fm
    album_name, asset_name, title, playing_status = lastfm()
    sleep(15)

    if old_title == "": #edge case
        #update RPC with title of song, playing status, start time, and album art + album name
        RPC.update(state=title, details="Listening to:",
        large_image=asset_name, large_text=album_name, 
        small_image='lollypop', small_text="Lollypop Music Player")
        old_title = title
        continue

    if old_title != title and playing_status == True:
        #update RPC with title of song, playing status, start time, and album art + album name
        RPC.update(state=title, details="Listening to:",
        large_image=asset_name, large_text=album_name, 
        small_image='lollypop', small_text="Lollypop Music Player")
        old_title = title
        continue

    elif playing_status == False:
        RPC.clear()
        continue

    #if track is same as track from previous check, do not update
    if old_title == title:
        continue

    else:
        RPC.clear()
        continue