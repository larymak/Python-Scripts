import pafy, pyglet
import os

def playMedia(songUrl):
    url = songUrl
    info = pafy.new(url)
    audio = info.getbestaudio(preftype="m4a")
    audio.download('song2.m4a', quiet=True)
    song = pyglet.media.load('song2.m4a')
    player = pyglet.media.Player()
    player.queue(song)
    while True:
        player.play()

       
playMedia(input("Please give song URL : "))
