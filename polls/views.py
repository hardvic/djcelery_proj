# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.conf.urls import url

from django.http import HttpResponse, JsonResponse

from djcelery.models import PeriodicTask, IntervalSchedule
from polls.tasks import add as add_t, mul as mul_t
# Create your views here.


def index(request):
    return HttpResponse("hi you're in index")


def add(request):
    result = {}
    result['x'] = request.GET.get('x')
    result['y'] = request.GET.get('y')
    result['result'] = add_t.delay(result['x'], result['y'])
    return HttpResponse(result, content_type='text/json')


def mul(request):
    result = {}
    result['x'] = request.GET.get('x')
    result['y'] = request.GET.get('y')
    result['result'] = mul_t.delay(result['x'], result['y'])
    return HttpResponse(result, content_type='text/json')


def get_all_tasks(request):
    all_periodic_task = PeriodicTask.objects.all()
    return HttpResponse(all_periodic_task, content_type='text/json')


def get_target_tasks_by_name(request):
    result = PeriodicTask.objects.filter(name='add_test_0829')
    return HttpResponse(result, content_type='text/json')


def update_tasks_interval(request):
    result, create = PeriodicTask.objects.get_or_create(name='liuquan_123')
    if create:
        interval = IntervalSchedule.objects.create(every=5, period='seconds')
        interval.save()
        result.interval = interval
        result.enabled = True
        result.save()
    else:
        result.interval.every = 5
        result.interval.save()
        result.enabled = True
        result.save()
    return HttpResponse(result, content_type='text/json')


