# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)

    def __unicode__(self):  # Python2的用法；
        # def __str__(self):   Python3的用法；
        return self.title
