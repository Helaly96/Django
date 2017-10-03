# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

class Album (models.Model):
    artist = models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.FileField(null=True)

    def get_absolute_url(self):

        return reverse("music:details", kwargs={"pk":self.pk})

    #el line of code elly fo2 dah by2oli , lma yt3mel object gded, ro7 ll details then add el primary key dah

    def __str__(self):
        return self.album_title + "-" + self.artist




class Song (models.Model):
    album =models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)
    #lma t3'eer attribute lazem t3ml migrate taniiiii , w ba3den t2fl el server and restart it:)

    def __str__(self):
        return self.song_title



