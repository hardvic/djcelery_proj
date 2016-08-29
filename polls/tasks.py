# !/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from celery import shared_task
from celery import task
# from djcelery_pro.celery import app


@task
def add_1(x, y):
    return x + y


@shared_task
def add_2(x, y):
    return x + y


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def test(numbers):
    chain(add_1(1, 2) | add_2(4) | mul(5))().get()

