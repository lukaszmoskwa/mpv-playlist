# mpv-playlist

## What

This application is a little wrapper in python to create a customized playlist from youtube to be played with mpv. It was delevoped with python3 and GTK3.0

## Requirements

In order to use this application, you have to install

```
python3
mpv

```

## Installation

The fastest way to install this application is directly by cloning the entire repository

```bash
git clone https://github.com/Lykos94/mpv-playlist.git

```

You can even only download just the mpv-playlist python file and set appropriate permissions. In order to work correct be sure that this is the structure of the folder containing the application.

```bash
|-	mpv-playlist
|-	icons/
|-	lista

```
Where *icons* is the folder where all the icons will be automatically stored. In a future implementation I'll add their auto removal.

*lista* is the file where your playlist is actually saved on. Like in this repo example, just add on each line a YouTube url in order to add it to your playlist.

## Usage

Run the application. As you will see a new indicator will appear in your bar and when clicked will display 2 options, Playlist and Quick.

As said, I'll implement an easier way to insert your preferred videos in the list, for now it is just manual.

## Screenshots

![](https://i.imgur.com/bNBfnWM.png)

#Todo
+ Automatic play when a video ends
+ Adding link to list from a input form in the graphical playlist
