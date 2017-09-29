# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Album

def index(request):
    all_albums=Album.objects.all()
    context={'all_albums': all_albums}
    return render(request, 'music/index.html', context)

# Create your views here.
