#!/usr/bin/env python

import json
import urllib.request
from PIL import Image

with open('/home/[USER]/.config/Google Play Music Desktop Player/json_store/playback.json') as json_file:
    data = json.load(json_file)
    album = data['song']['album']
    art =  data['song']['albumArt']

b = str(album)


f = open("/home/peter/.nowplaying/album.txt", "r")
contents = f.readline().rstrip('/n')
f.close()

testequality = None

for i in range(0,min(len(b),len(contents))):
    if b[i] != contents[i]:
        testequality = False
        break
    else:
        testequality = True

if not testequality:
    urllib.request.'urlretrieve(art, "/home/peter/.nowplaying/album.jpg")
    image = "/home/peter/.nowplaying/album.jpg"
    im1 = Image.open(image)
    im5 = im1.resize((70, 70), Image.ANTIALIAS)
    im5.save("/home/peter/.nowplaying/album.jpg")

f = open("/home/peter/.nowplaying/album.txt", "w")
f.write(b)
f.close()
