#!/usr/bin/env python

import json

with open('/home/[USER]/.config/Google Play Music Desktop Player/json_store/playback.json') as json_file:
    data = json.load(json_file)
    title =  data['song']['title']
    artist = data['song']['artist']
    album = data['song']['album']

t = str(title)
a = str(artist)
b = str(album)

if t == 'None':
    np = str(' ')
elif data['playing']:
    np = str('Now playing:   ' + t + ' - ' + a + ' (' + b + ')')
else:
    np = str('Paused:   ' + t + ' - ' + a + ' (' + b + ')')

print np
