# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=rbJjpU6BEps'])