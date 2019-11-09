import json

with open('/home/[USER]/.config/Google Play Music Desktop Player/json_store/playback.json') as json_file:
    data = json.load(json_file)
    title =  data['song']['title']
    artist = data['song']['artist']
    album = data['song']['album']

np = title + ' - ' + artist + ' (' + album + ')'

print(np)

file = open('/home/[USER]/.nowplaying', 'w')
file.write(np)
file.close()
