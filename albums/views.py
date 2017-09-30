# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import AsameterAlbums

def index(request):
    all_albums=AsameterAlbums.objects.all()
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        if album.master_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.master_10*51)
        else:
            album.redcolor=int((10-album.master_10)*51)
            album.greencolor=int(255)
    context={'all_albums': all_albums}
    return render(request, 'albums/index.html', context)

def sortfavorite(request):
    all_albums=AsameterAlbums.objects.all()
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        if album.master_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.master_10*51)
        else:
            album.redcolor=int((10-album.master_10)*51)
            album.greencolor=int(255)
    all_albums_sorted=sorted(all_albums, key=lambda x: x.master_10, reverse=True)
    context={'all_albums': all_albums_sorted}
    return render(request, 'albums/index.html', context)

def sortalbum(request):
    all_albums=AsameterAlbums.objects.all()
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        if album.master_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.master_10*51)
        else:
            album.redcolor=int((10-album.master_10)*51)
            album.greencolor=int(255)
    all_albums_sorted=sorted(all_albums, key=lambda x: x.album)
    context={'all_albums': all_albums_sorted}
    return render(request, 'albums/index.html', context)

def sortartist(request):
    all_albums=AsameterAlbums.objects.all()
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        if album.master_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.master_10*51)
        else:
            album.redcolor=int((10-album.master_10)*51)
            album.greencolor=int(255)
    all_albums_sorted=sorted(all_albums, key=lambda x: x.artist)
    context={'all_albums': all_albums_sorted}
    return render(request, 'albums/index.html', context)

def sortgenre(request):
    all_albums=AsameterAlbums.objects.all()
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        if album.master_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.master_10*51)
        else:
            album.redcolor=int((10-album.master_10)*51)
            album.greencolor=int(255)
    all_albums_sorted=sorted(all_albums, key=lambda x: x.genre)
    context={'all_albums': all_albums_sorted}
    return render(request, 'albums/index.html', context)
# Create your views here.
