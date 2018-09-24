#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: myblog 
# Software: PyCharm
# Time    : 2018-09-24 11:37
# File    : urls.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from django.conf.urls import url
from django.contrib import admin
from . import views

# from blog import views
# import blog.views as bv

urlpatterns = [
    url(r'^index/$', views.index),
]
