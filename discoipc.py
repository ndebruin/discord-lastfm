#!/usr/bin/python

from discoIPC import ipc
from lastfm import format_lastfm
from time import sleep, time
from os import getenv

from dotenv import load_dotenv
load_dotenv()

client = ipc.DiscordIPC(getenv("DISCORD"))


base_activity = {
    'details': 'For more info about this, please visit: https://git.draigon.org/ndebruin/lastfm-discord-rpc',
    'timestamps': {},
    'assets': {
        'small_image': 'lollypop',
        'small_text': 'Lollypop Music Player'
    }
}

def format_activity():
    album_name, asset_name, title = format_lastfm()

    activity = base_activity

    activity['state']= 'Listening to {0}'.format(title)
    activity['timestamps']['start'] = time()
    activity['assets']['large_image'] = asset_name
    activity['assets']['large_text']= album_name
    return activity


while True:

    client.connect()

    client.update_activity(format_activity())

    client.disconnect()

    sleep(60)
