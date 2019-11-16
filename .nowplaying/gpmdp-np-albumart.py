#!/usr/bin/env python

import json
import urllib
from PIL import Image

with open('/home/[USER]/.config/Google Play Music Desktop Player/json_store/playback.json') as json_file:
    data = json.load(json_file)
    album = data['song']['album']
    art =  str(data['song']['albumArt'])

b = str(album)

f = open("/home/[USER]/.nowplaying/album.txt", "r")
contents = f.readline().rstrip('/n')
f.close()

testequality = None

for i in range(0,min(len(b),len(contents))):
    if b[i] != contents[i]:
        testequality = False
        break
    else:
        testequality = True

if not testequality and art != None:
    image = str(urllib.urlretrieve(art, r"/home/[USER]/.nowplaying/album-large.jpg"))
    im1 = Image.open("/home/[USER]/.nowplaying/album-large.jpg")
    size = (50,50)
    im1 = im1.resize(size, Image.ANTIALIAS)
    im1.save("/home/[USER]/.nowplaying/album.jpg")

if not testequality and art != None:
    f = open("/home/[USER]/.nowplaying/album.txt", "w")
    f.write(b)
    f.close()
