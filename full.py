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
previous_title_old = ""
old_album = ""
old_asset = ""
paused_counter = 0

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
        'limit': '2',
        'format': 'json'
    }

    response = get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)

    names_dict = json_loads(open('names-dict.txt', 'r').read())

    response = dict(response.json())
    nowplaying = response["recenttracks"]["track"][0]
    album_name = nowplaying["album"]["#text"]
    title = nowplaying["name"]
    previous_title = response["recenttracks"]["track"][1]["name"]

    if album_name == "":
        album_name = "Cupcake Landers"

    if previous_title == "":
        previous_title = "Cupcake Landers"
    
    print(response)
    #print("request completed")
    return album_name, names_dict[album_name], title, previous_title

#keep program constantly running
while True:
    sleep(15)
    #get new data from last.fm
    album_name, asset_name, title, previous_title = lastfm()
    print(title)
    print(old_title)

    if old_title == "":
        #update RPC with title of song, playing status, start time, and album art + album name
        RPC.update(state="Listening to {}".format(title), details="Playing", start=time(), 
        large_image=asset_name, large_text=album_name, 
        small_image='lollypop', small_text="Lollypop Music Player")
        old_title = title
        old_album = album_name
        old_asset = asset_name
        print("edge case")
        continue

    if old_title != title and old_title == previous_title:
        #update RPC with title of song, playing status, start time, and album art + album name
        RPC.update(state="Listening to {}".format(title), details="Playing", start=time(), 
        large_image=asset_name, large_text=album_name, 
        small_image='lollypop', small_text="Lollypop Music Player")
        old_title = title
        old_album = album_name
        old_asset = asset_name
        print("new track")
        continue
        
    elif old_title != title and old_title != previous_title and paused_counter == 20:
        RPC.clear()
        paused_counter = 0
        print("rich presence stopped")
        continue

    elif old_title != title and old_title != previous_title:
        #assume paused track
        #update RPC to reflect paused status
        RPC.update(state="Listening to {}".format(old_title), details="Paused", end=time(), 
        large_image=old_asset, large_text=old_album, 
        small_image='lollypop', small_text="Lollypop Music Player")
        #iterate paused counter for five minute timeout
        paused_counter = paused_counter + 1
        print("paused status")
        continue

    #if track is same as track from previous check, do not update
    if old_title == title:
        print("same track")
        continue

    else:
        RPC.clear()
        continue