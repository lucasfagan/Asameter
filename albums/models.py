# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Album(models.Model):
    #date=models.Date #WHAT IS CORRECT SYNTAX
    album_title=models.CharField(max_length=200)

    explicit=models.CharField(max_length=5)


# Create your models here.
