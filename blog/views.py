# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blog import models

# Create your views here.

def index(request):
    # return HttpResponse('Hello World!cuixiaozhao')
    # return render(request, 'blog/index.html', {'hello': 'Hello,Django Blog!'})
    #article = models.Article.objects.get(pk=3)
    articles = models.Article.objects.all()
    print(articles)
    return render(request,'blog/index.html',{'articles':articles})
