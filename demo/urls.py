#!/usr/bin/python
from django.conf.urls import url

from demo.views import index


app_name = 'demo'

urlpatterns = [
    url(r'^$', index, name='index'),
]
