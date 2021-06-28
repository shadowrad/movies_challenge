# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from movies.helpers import int_to_Roman


class Person(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=150, null=False)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Movie(models.Model):
    title = models.CharField(max_length=250)
    release_year = models.IntegerField()
    casting = models.ManyToManyField(Person, related_name='movies_as_actors')
    directors = models.ManyToManyField(Person, related_name='movies_as_directors')
    producers = models.ManyToManyField(Person, related_name='movies_as_producers')

    def roman_year(self):
        return int_to_Roman(self.release_year)



class PersonAlias(models.Model):
    name = models.CharField(max_length=100)
    person = models.ForeignKey(Person, related_name='aliases', on_delete=models.CASCADE)
