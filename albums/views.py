# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import AsameterAlbums

globaldata=AsameterAlbums.objects.all()
globalsearchterm=""

def index(request):
    global globaldata
    globaldata=AsameterAlbums.objects.all()
    global globalsearchterm
    globalsearchterm=""
    all_albums=globaldata
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        album.name_no_spaces=album.album.replace(" ","-")
        if album.master_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.master_10*51)
        else:
            album.redcolor=int((10-album.master_10)*51)
            album.greencolor=int(255)
    context={'all_albums': all_albums}
    return render(request, 'albums/index.html', context)

#if no search, this is the same as index (because it is automatically sorted by date)
def sortdate(request):
    all_albums=globaldata
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        album.name_no_spaces=album.album.replace(" ","-")
        if album.master_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.master_10*51)
        else:
            album.redcolor=int((10-album.master_10)*51)
            album.greencolor=int(255)
    all_albums_sorted=sorted(all_albums, key=lambda x: x.date)
    context={'all_albums': all_albums_sorted, 'search_term': globalsearchterm}
    return render(request, 'albums/index.html', context)

def sortfavorite(request):
    all_albums=globaldata
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        album.name_no_spaces=album.album.replace(" ","-")
        if album.master_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.master_10*51)
        else:
            album.redcolor=int((10-album.master_10)*51)
            album.greencolor=int(255)
    all_albums_sorted=sorted(all_albums, key=lambda x: x.master_10, reverse=True)
    context={'all_albums': all_albums_sorted, 'search_term': globalsearchterm}
    return render(request, 'albums/index.html', context)

def sortalbum(request):
    all_albums=globaldata
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        album.name_no_spaces=album.album.replace(" ","-")
        if album.master_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.master_10*51)
        else:
            album.redcolor=int((10-album.master_10)*51)
            album.greencolor=int(255)
    all_albums_sorted=sorted(all_albums, key=lambda x: x.album)
    context={'all_albums': all_albums_sorted, 'search_term': globalsearchterm}
    return render(request, 'albums/index.html', context)

def sortartist(request):
    all_albums=globaldata
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        album.name_no_spaces=album.album.replace(" ","-")
        if album.master_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.master_10*51)
        else:
            album.redcolor=int((10-album.master_10)*51)
            album.greencolor=int(255)
    all_albums_sorted=sorted(all_albums, key=lambda x: x.artist)
    context={'all_albums': all_albums_sorted, 'search_term': globalsearchterm}
    return render(request, 'albums/index.html', context)

def sortgenre(request):
    all_albums=globaldata
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        album.name_no_spaces=album.album.replace(" ","-")
        if album.master_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.master_10*51)
        else:
            album.redcolor=int((10-album.master_10)*51)
            album.greencolor=int(255)
    all_albums_sorted=sorted(all_albums, key=lambda x: x.genre)
    context={'all_albums': all_albums_sorted, 'search_term': globalsearchterm}
    return render(request, 'albums/index.html', context)

def detail(request, selected_album):
    specific_album=get_object_or_404(AsameterAlbums, album__iexact=selected_album.replace("-"," "))
    context={}
    if globalsearchterm!="":
        context['search_term']=globalsearchterm
    context['specific_album']=specific_album
    return render(request, 'albums/detail.html', context)

def search(request):
    global globaldata
    global globalsearchterm
    context={}
    if request.method == "POST":
        globalsearchterm=request.POST.get("searchbar", None)
    context['search_term']=globalsearchterm
    refined_data=AsameterAlbums.objects.filter(album__istartswith=globalsearchterm)
    refined_data2=AsameterAlbums.objects.filter(artist__istartswith=globalsearchterm)
    refined_data3=AsameterAlbums.objects.filter(genre__istartswith=globalsearchterm)
    refined_data4=AsameterAlbums.objects.filter(master_10__istartswith=globalsearchterm)
    refined_data5=AsameterAlbums.objects.filter(album__icontains=globalsearchterm)
    refined_data6=AsameterAlbums.objects.filter(artist__icontains=globalsearchterm)
    refined_data7=AsameterAlbums.objects.filter(genre__icontains=globalsearchterm)
    refined_data8=AsameterAlbums.objects.filter(master_10__icontains=globalsearchterm)
    globaldata = refined_data | refined_data2 | refined_data3 | refined_data4 | refined_data5 | refined_data6 | refined_data7 | refined_data8
    for album in globaldata:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        album.name_no_spaces=album.album.replace(" ","-")
        if album.master_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.master_10*51)
        else:
            album.redcolor=int((10-album.master_10)*51)
            album.greencolor=int(255)
    context['all_albums']=globaldata
    return render(request, 'albums/index.html', context)

def main(request):
    context={}
    return render(request, 'albums/main.html', context)
# Create your views here.
