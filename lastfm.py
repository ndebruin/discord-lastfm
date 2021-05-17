#!/usr/bin/python

from os import getenv
from requests import get
from time import sleep

from dotenv import load_dotenv
load_dotenv()

names_dict = {
    "Hawaii: Part II: Part ii": "hawaii_part_ii_part_ii",
    "Hawaii: Part II": "hawaii_part_ii",
    "Hawaii Partii": "hawaii_partii",
    
    "Pray for the Wicked": "pray_for_the_wicked",
    
    "Good and Evil": "good_and_evil",
    "Marvin's Marvelous Mechanical Museum": "marvins_marvelous_mechanical_museum",
    
    "Airplanes": "airplanes",
    "Rain": "rain",
    "Extended Play": "extended_play",
    "Strangely Arousing": "strangely_arousing",
    
    "Almost Tropical EP": "almost_tropical_ep",
    "Heaven Force Early Fall EP": "None",
    
    "Oncle Jazz": "oncle_jazz",
    "Retro Grooves, Vol. 3": "retro_grooves_vol_3",
    
    "Matilda the Musical": "matilda",
    "Footloose": "footloose",
    "Come From Away": "come_from_away",
    "Fiddler on the Roof": "fiddler_on_the_roof",
    
    "Cupcake Landers": "cupcake_landers",
    
    "Fossil Fighters": "fossil_fighters",
    
    "Terraria Soundtrack Volume 1": "terraria_soundtrack_volume_1",
    "Terraria Soundtrack Volume 2": "terraria_soundtrack_volume_2",
    "Terraria Soundtrack Volume 3": "terraria_soundtrack_volume_3",
    "Terraria Soundtrack Volume 4": "terraria_soundtrack_volume_4",
    "Portal": "portal",
    "Portal 2: Songs to Test By - Volume 1": "portal_2",
    "Portal 2: Songs to Test By - Volume 2": "portal_2",
    "Portal 2: Songs to Test By - Volume 3": "portal_2",
    "Portal Stories: Mel Soundtrack": "portal_stories_mel"

}

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
recent_tracks = response["recenttracks"]
tracks = recent_tracks["track"]
nowplaying = tracks[0]
album = nowplaying["album"]
album_name = album["#text"]
title = nowplaying["name"]
if album_name == "":
    album_name = "Cupcake Landers"

print("{}({}) - {}".format(album_name, names_dict[album_name], title))
#print("{} - {}".format(names_dict[albumName], title))
