#!/usr/bin/python

# a very simple test using pypresence

from pypresence import Presence # The simple rich presence client in pypresence
import time
from os import getenv

from dotenv import load_dotenv
load_dotenv()

client_id = getenv("DISCORD")
RPC = Presence(client_id)  # Initialize the Presence client

RPC.connect()
print("connected")

RPC.update(state="Rich Presence using pypresence!", pid=1) # Updates our presence
print("presence?")

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds