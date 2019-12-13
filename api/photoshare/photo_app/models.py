# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Country(models.Model):
    country_name = models.CharField('Name of Country', max_length=120)
    


class Photo(models.Model):
    id_photo = models.PrimaryKey()
    time_photo_taken = models.DateTimeField('date photo taken')
    latitude =  models.CharField('Latitude of Photo Taken', max_length=120)
    longitude = models.CharField('Longitude of Photo Taken', max_length=120)


class User(models.Model):
    email  = models.CharField(, max_length=120)

