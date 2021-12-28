# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class Pokemon(models.Model):
    nombre = models.CharField(max_length=50)
    sprite = models.ImageField(upload_to="sprites")
    detalles = models.CharField(max_length=50)