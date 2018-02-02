#!/usr/bin/python3

from subprocess import call
import tkinter


filename = "lista"

with open(filename) as f:
    content = f.readlines()
print(str(content))

call(["mpv", content[0]])
