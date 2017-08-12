# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Trailers class
class Movies(models.Model):
    # Movie title
    title = models.CharField(max_length=50)
    # Trailer poster (ex: google.com/moana.jpg)
    poster_image_url = models.CharField(max_length=300)
    # YouTube trailer video
    trailer_youtube_url = models.CharField(max_length=300)
    # YouTube trailer ID
    trailer_youtube_id = models.CharField(max_length=20)

    # String representation for the class
    def __str__(self):
        return self.title
