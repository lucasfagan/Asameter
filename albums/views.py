# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import AsameterAlbums

globaldata=AsameterAlbums.objects.all()
globalsearchterm=""
globalfilter=""
globalfilterascending=False

def index(request):
    global globaldata
    globaldata=AsameterAlbums.objects.all()
    global globalsearchterm
    globalsearchterm=""
    global globalfilter
    global globalfilterascending
    globalfilter=""
    globalfilterascending=False;
    all_albums=globaldata
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        album.name_no_spaces=album.album.replace(" ","-")
        if album.music_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.music_10*51)
        else:
            album.redcolor=int((10-album.music_10)*51)
            album.greencolor=int(255)
    context={'all_albums': all_albums}
    return render(request, 'albums/index.html', context)

#if no search, this is the same as index (because it is automatically sorted by date)
def sortdate(request):
    global globalfilter
    global globalfilterascending
    all_albums=globaldata
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        album.name_no_spaces=album.album.replace(" ","-")
        if album.music_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.music_10*51)
        else:
            album.redcolor=int((10-album.music_10)*51)
            album.greencolor=int(255)
    if globalfilter=="date":
        if globalfilterascending==True:
            all_albums_sorted=sorted(all_albums, key=lambda x: x.date)
            globalfilterascending=False;
        else:
            all_albums_sorted=sorted(all_albums, key=lambda x: x.date, reverse=True)
            globalfilterascending=True;
    else:
        all_albums_sorted=sorted(all_albums, key=lambda x: x.date, reverse=True)
        globalfilterascending=True;
    globalfilter="date"

    context={'all_albums': all_albums_sorted, 'search_term': globalsearchterm}
    return render(request, 'albums/index.html', context)

def sortfavorite(request):
    all_albums=globaldata
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        album.name_no_spaces=album.album.replace(" ","-")
        if album.music_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.music_10*51)
        else:
            album.redcolor=int((10-album.music_10)*51)
            album.greencolor=int(255)
    global globalfilter
    global globalfilterascending
    if globalfilter=="score":
        if globalfilterascending==True:
            all_albums_sorted=sorted(all_albums, key=lambda x: x.music_10)
            globalfilterascending=False;
        else:
            all_albums_sorted=sorted(all_albums, key=lambda x: x.music_10, reverse=True)
            globalfilterascending=True;
    else:
        all_albums_sorted=sorted(all_albums, key=lambda x: x.music_10, reverse=True)
        globalfilterascending=True;
    globalfilter="score"
    context={'all_albums': all_albums_sorted, 'search_term': globalsearchterm}
    return render(request, 'albums/index.html', context)

def sortalbum(request):
    all_albums=globaldata
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        album.name_no_spaces=album.album.replace(" ","-")
        if album.music_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.music_10*51)
        else:
            album.redcolor=int((10-album.music_10)*51)
            album.greencolor=int(255)
    global globalfilter
    global globalfilterascending
    if globalfilter=="album":
        if globalfilterascending==True:
            all_albums_sorted=sorted(all_albums, key=lambda x: x.album)
            globalfilterascending=False;
        else:
            all_albums_sorted=sorted(all_albums, key=lambda x: x.album, reverse=True)
            globalfilterascending=True;
    else:
        all_albums_sorted=sorted(all_albums, key=lambda x: x.album, reverse=True)
        globalfilterascending=True;
    globalfilter="album"
    context={'all_albums': all_albums_sorted, 'search_term': globalsearchterm}
    return render(request, 'albums/index.html', context)

def sortartist(request):
    all_albums=globaldata
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        album.name_no_spaces=album.album.replace(" ","-")
        if album.music_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.music_10*51)
        else:
            album.redcolor=int((10-album.music_10)*51)
            album.greencolor=int(255)
    global globalfilter
    global globalfilterascending
    if globalfilter=="artist":
        if globalfilterascending==True:
            all_albums_sorted=sorted(all_albums, key=lambda x: x.artist)
            globalfilterascending=False;
        else:
            all_albums_sorted=sorted(all_albums, key=lambda x: x.artist, reverse=True)
            globalfilterascending=True;
    else:
        all_albums_sorted=sorted(all_albums, key=lambda x: x.artist, reverse=True)
        globalfilterascending=True;
    globalfilter="artist"
    context={'all_albums': all_albums_sorted, 'search_term': globalsearchterm}
    return render(request, 'albums/index.html', context)

def sortgenre(request):
    all_albums=globaldata
    for album in all_albums:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        album.name_no_spaces=album.album.replace(" ","-")
        if album.music_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.music_10*51)
        else:
            album.redcolor=int((10-album.music_10)*51)
            album.greencolor=int(255)
    global globalfilter
    global globalfilterascending
    if globalfilter=="genre":
        if globalfilterascending==True:
            all_albums_sorted=sorted(all_albums, key=lambda x: x.genre)
            globalfilterascending=False;
        else:
            all_albums_sorted=sorted(all_albums, key=lambda x: x.genre, reverse=True)
            globalfilterascending=True;
    else:
        all_albums_sorted=sorted(all_albums, key=lambda x: x.genre, reverse=True)
        globalfilterascending=True;
    globalfilter="genre"
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
    searchmodifier=""
    context={}
    if request.method == "POST":
        globalsearchterm=request.POST.get("searchbar", None)
        if ":" in globalsearchterm:
            index=globalsearchterm.index(':')
            searchmodifier=globalsearchterm[:index]
            globalsearchterm=globalsearchterm[index+1:]
    print(searchmodifier.upper())
    if searchmodifier.upper() in ['ALBUM','GENRE','SCORE','ARTIST']:
        context['modifier']=searchmodifier.lower().capitalize()
        if searchmodifier.upper()=='ALBUM':
            refined_data=AsameterAlbums.objects.filter(album__istartswith=globalsearchterm)
            refined_data5=AsameterAlbums.objects.filter(album__icontains=globalsearchterm)
            globaldata=refined_data | refined_data5
        if searchmodifier.upper()=='GENRE':
            refined_data3=AsameterAlbums.objects.filter(genre__istartswith=globalsearchterm)
            refined_data7=AsameterAlbums.objects.filter(genre__icontains=globalsearchterm)
            globaldata=refined_data3 | refined_data7
        if searchmodifier.upper()=='SCORE':
            refined_data4=AsameterAlbums.objects.filter(music_10__istartswith=globalsearchterm)
            refined_data8=AsameterAlbums.objects.filter(music_10__icontains=globalsearchterm)
            globaldata=refined_data4 | refined_data8
        else:
            refined_data2=AsameterAlbums.objects.filter(artist__istartswith=globalsearchterm)
            refined_data6=AsameterAlbums.objects.filter(artist__icontains=globalsearchterm)
            globaldata=refined_data2 | refined_data6

    else:
        refined_data=AsameterAlbums.objects.filter(album__istartswith=globalsearchterm)
        refined_data2=AsameterAlbums.objects.filter(artist__istartswith=globalsearchterm)
        refined_data3=AsameterAlbums.objects.filter(genre__istartswith=globalsearchterm)
        refined_data4=AsameterAlbums.objects.filter(music_10__istartswith=globalsearchterm)
        refined_data5=AsameterAlbums.objects.filter(album__icontains=globalsearchterm)
        refined_data6=AsameterAlbums.objects.filter(artist__icontains=globalsearchterm)
        refined_data7=AsameterAlbums.objects.filter(genre__icontains=globalsearchterm)
        refined_data8=AsameterAlbums.objects.filter(music_10__icontains=globalsearchterm)
        globaldata = refined_data | refined_data2 | refined_data3 | refined_data4 | refined_data5 | refined_data6 | refined_data7 | refined_data8

    context['search_term']=globalsearchterm

    for album in globaldata:
        album.album=album.album.capitalize()
        album.artist=album.artist.capitalize()
        album.genre=album.genre.capitalize()
        album.name_no_spaces=album.album.replace(" ","-")
        if album.music_10<=5:
            album.redcolor=int(255)
            album.greencolor=int(album.music_10*51)
        else:
            album.redcolor=int((10-album.music_10)*51)
            album.greencolor=int(255)
    context['all_albums']=globaldata
    return render(request, 'albums/index.html', context)

def main(request):
    context={}
    return render(request, 'albums/main.html', context)
# Create your views here.
