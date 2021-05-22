#!/usr/bin/python

from lastfm import format_lastfm
from pypresence import Presence
from os import getenv
from time import sleep, time

client_id = getenv("DISCORD")

old_title = ""

RPC = Presence(client_id)
RPC.connect()

while True:
    album_name, asset_name, title = format_lastfm()

    if old_title == title:
        continue
    else:
        RPC.update(state="Listening to {}".format(title), start=time(), 
        large_image=asset_name, large_text=album_name, 
        small_image='lollypop', small_text="Lollypop Music Player")
        old_title = title

    sleep(15)