# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 02:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_logo',
        ),
    ]