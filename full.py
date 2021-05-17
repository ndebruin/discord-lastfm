#!/usr/bin/python

from lastfm import format_lastfm
from pypresence import Presence, Client
from os import getenv
from time import sleep

client_id = getenv("DISCORD")
#RPC = Presence(client_id=client_id)
#RPC.connect()


client = Client(client_id)
client.start()
auth = client.authorize(client_id, ['rpc'])
print(auth)

#client.authenticate("0TFY-yq5u9Nsa6_yeH1rGIUk42f8oRHi")
print("connected")

while True:
    album_name, asset_name, title = format_lastfm()
    try:
        client.set_activity(large_image=str(asset_name), large_text=str(album_name), state="Listening to ", details=str(title))
    except Exception as e:
        print("fuck me")
    sleep(60)