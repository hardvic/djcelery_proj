# !/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from polls import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^mul$', views.mul, name='mul'),
    url(r'all_tasks', views.get_all_tasks, name='all_tasks'),
    url(r'get_by_name', views.get_target_tasks_by_name, name='get_by_name'),
    url(r'update_tasks', views.update_tasks_interval, name='update_tasks'),
]



