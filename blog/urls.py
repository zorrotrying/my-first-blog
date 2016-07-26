# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:55:43 2016

@author: zouro2
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]