# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 15:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trailer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='image',
            new_name='poster_image_url',
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='trailer',
            new_name='trailer_youtube_url',
        ),
    ]
