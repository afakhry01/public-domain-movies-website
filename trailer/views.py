# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movies
import re


def index(request):
    all_movies = Movies.objects.all()

    # Extract the youtube ID from the url
    def youtube_id(url):
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', url)
        trailer_id = (youtube_id_match.group(0) if youtube_id_match else None)
        return trailer_id

    # Insert youtube ID into database
    for movie in all_movies:
        movie.trailer_youtube_id = youtube_id(movie.trailer_youtube_url)

    # Create dictionary and render template
    context = {'all_movies': all_movies,
               'trailer_youtube_id': Movies.trailer_youtube_id,
               'poster_image_url': Movies.poster_image_url,
               'movie_title': Movies.title
               }
    return render(request, 'trailer\index.html', context)
