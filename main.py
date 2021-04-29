import requests
import json
from time import sleep

h = {"authorization": open("token").read().strip("\n "),
 "content-type": "application/json"}

def update(s):
    data = json.dumps({"custom_status":{"text":s,"emoji_name":"🎬"}})
    return requests.patch("https://discord.com/api/v9/users/@me/settings", data=data, headers=h)
     
window = 10

orig = "I like to do stuff with code, can you tell?"
orig += " " * window
orig = orig.replace(" ", "_")

i = 0
while 1:
    s = orig[i:i+window]
    if len(s) != window:
        s += orig[:window-len(s)]
    update(s)
    print(s, end="\r")
    sleep(.25)
    i += 1
    if i == len(orig):
        i = 0
