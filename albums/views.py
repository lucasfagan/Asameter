# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import AsameterAlbums

globaldata=AsameterAlbums.objects.all()
globalsearchterms={}
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
        album.redscore=int(25.5*album.music_10)
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
    context={}
    if request.method == "POST":
        globalsearchterm=request.POST.get("searchbar", None)
    searchdictionary=splitstring(globalsearchterm)
    #put in here something like if and exists
    if 'and' in searchdictionary.keys():
        if searchdictionary['and']=='Y':
            del searchdictionary['and']
            updateddata=AsameterAlbums.objects.all()
            for key in searchdictionary.keys():
                if key.upper()=='ALBUM':
                    updateddata=updateddata.filter(album__istartswith=str(searchdictionary[key])) | updateddata.filter(album__icontains=key)
                elif key.upper()=='GENRE':
                    updateddata=updateddata.filter(genre__istartswith=str(searchdictionary[key])) | updateddata.filter(genre__icontains=str(searchdictionary[key]))
                elif key.upper()=='SCORE':
                    updateddata=updateddata.filter(music_10__istartswith=str(searchdictionary[key])) | updateddata.filter(music_10__icontains=str(searchdictionary[key]))
                elif key.upper()=='ARTIST':
                    updateddata=updateddata.filter(artist__istartswith=str(searchdictionary[key])) | updateddata.filter(artist__icontains=str(searchdictionary[key]))
                else:
                    data=updateddata.filter(album__istartswith=str(searchdictionary[key]))
                    data2=updateddata.filter(artist__istartswith=str(searchdictionary[key]))
                    data3=updateddata.filter(genre__istartswith=str(searchdictionary[key]))
                    data4=updateddata.filter(music_10__istartswith=str(searchdictionary[key]))
                    data5=updateddata.filter(album__icontains=str(searchdictionary[key]))
                    data6=updateddata.filter(artist__icontains=str(searchdictionary[key]))
                    data7=updateddata.filter(genre__icontains=str(searchdictionary[key]))
                    data8=updateddata.filter(music_10__icontains=str(searchdictionary[key]))
                    updateddata=data|data2|data3|data4|data5|data6|data7|data8
                globaldata=updateddata
        else:
            del searchdictionary['and']
        #trying to get empty QuerySet (no internet to look at documentation)
            print(searchdictionary)
            finaldata=AsameterAlbums.objects.filter(music_10__startswith='fdasdsasds')
            for key in searchdictionary.keys():
                if key.upper()=='ALBUM':
                    #problem w finaldata here
                    finaldata=finaldata|AsameterAlbums.objects.filter(album__istartswith=str(searchdictionary[key])) | AsameterAlbums.objects.filter(album__icontains=str(searchdictionary[key]))
                elif key.upper()=='GENRE':
                    finaldata=finaldata|AsameterAlbums.objects.filter(genre__istartswith=str(searchdictionary[key])) | AsameterAlbums.objects.filter(genre__icontains=str(searchdictionary[key]))
                elif key.upper()=='SCORE':
                    finaldata=finaldata|AsameterAlbums.objects.filter(music_10__istartswith=str(searchdictionary[key])) | AsameterAlbums.objects.filter(music_10__icontains=str(searchdictionary[key]))
                elif key.upper()=='ARTIST':
                    finaldata=finaldata|AsameterAlbums.objects.filter(artist__istartswith=str(searchdictionary[key])) | AsameterAlbums.objects.filter(artist__icontains=str(searchdictionary[key]))
                else:
                    print("no key")
                    data1=AsameterAlbums.objects.filter(album__istartswith=key)
                    data2=AsameterAlbums.objects.filter(artist__istartswith=key)
                    data3=AsameterAlbums.objects.filter(genre__istartswith=key)
                    data4=AsameterAlbums.objects.filter(music_10__istartswith=key)
                    data5=AsameterAlbums.objects.filter(album__icontains=key)
                    data6=AsameterAlbums.objects.filter(artist__icontains=key)
                    data7=AsameterAlbums.objects.filter(genre__icontains=key)
                    data8=AsameterAlbums.objects.filter(music_10__icontains=key)
                    finaldata=data1|data2|data3|data4|data5|data6|data7|data8
            globaldata=finaldata
            print(finaldata)
        context['search_term']=globalsearchterm
    else:
        globaldata=AsameterAlbums.objects.all()
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

def splitstring(s):
    #use same modifier multiple times
    if s=="":
        return {}
    searchtermdict={}
    index1=0
    index2=0
    for z in range(0,len(s)):
        if s[z]=="[":
            index1=z
        elif s[z]=="]":
            index2=z
    if index2!=0:
        if s[index1+1:index2].lower()=="and":
            searchtermdict['and']='Y'
        else:
            searchtermdict['and']='N'
        s=s[0:index1]+s[index2+1:len(s)]
    else:
        searchtermdict['and']='N'
        s=s[0:index1]+s[index2:len(s)]
    if s[len(s)-1]==" ":
        s=s[:len(s)-1]
    lastchar=0
    for x in range(0,len(s)):
        if s[x]==";" or x==len(s)-1:
            if s[x]==";":
                substring=s[lastchar:x]
            else:
                substring=s[lastchar:x+1]
            if ":" in substring:
                colonindex=substring.index(":")
                searchtermdict[substring[:colonindex]]=substring[colonindex+1:]
            else:
                searchtermdict[substring]=""
            if x!=len(s)-1:
                y=x+1
                lastchar=y
                while s[y]==" ":
                    lastchar=y+1
                    y+=1
    return searchtermdict
# Create your views here.
