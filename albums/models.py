# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Album(models.Model):
    #date=models.Date #WHAT IS CORRECT SYNTAX
    date=models.DateField()
    album_title=models.CharField(max_length=200)
    artist=models.CharField(max_length=50)
    genre=models.CharField(max_length=35)
    master_score=FloatField()
    music_score=FloatField()
    tt=CharField(max_length=600)
    comments=CharField(max_length=600)
    explicit=models.CharField(max_length=5)
    release_date=models.DateField()

    def __str__(self):
        return self.album_title


# Create your models here.
