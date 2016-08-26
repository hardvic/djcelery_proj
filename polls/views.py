# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf.urls import url

from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("hi you're in index")

