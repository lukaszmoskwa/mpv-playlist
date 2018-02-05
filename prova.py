#!/usr/bin/python3

from subprocess import call
import tkinter


filename = "lista"

with open(filename) as f:
    content = f.readlines()
print(str(content))

def gimme_thumb(yt_url):
	stringa_di_prova = "https://img.youtube.com/vi/<insert-youtube-video-id-here>/0.jpg"
	stringa_da_eliminare = "?v="
	x = yt_url.split(stringa_da_eliminare)
	return "https://img.youtube.com/vi/" + x[1] + "/0.jpg"


print(gimme_thumb("https://www.youtube.com/watch?v=Q_QEPrkwZ-Q"))
#call(["mpv", content[0]])
