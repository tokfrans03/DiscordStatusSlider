import requests
import json
from time import sleep

h = {"authorization": open("token").read().strip("\n "),
 "content-type": "application/json"}

def update(s):
    data = json.dumps({"custom_status":{"text":s,"emoji_name":"🎬"}})
    return requests.patch("https://discord.com/api/v9/users/@me/settings", data=data, headers=h)
     
window = 10

orig = """_________According to all known laws
of aviation,

  
there is no way a bee
should be able to fly.

  
Its wings are too small to get
its fat little body off the ground.

  
The bee, of course, flies anyway

  
because bees don't care
what humans think is impossible.

  
Yellow, black. Yellow, black.
Yellow, black. Yellow, black.

  
Ooh, black and yellow!
Let's shake it up a little."""

orig = orig.replace("\n", " ")
while "  " in orig:
    orig = orig.replace("  ", " ")

orig += " " * window
orig = orig.replace(" ", "_")

i = 0
while 1:
    s = orig[i:i+window]
    if len(s) != window:
        s += orig[:window-len(s)]
    r = update(s)
    if "401: Unauthorized" in r.text:
        print(r.text)
        print("Token expired or wrong, find it in the authorization header in any discord web request")
    print(s, end="\r")
    sleep(.25)
    i += 1
    if i == len(orig):
        i = 0
