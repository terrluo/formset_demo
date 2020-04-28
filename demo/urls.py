#!/usr/bin/python
from django.conf.urls import url

from demo.views import index, book, book_list

app_name = 'demo'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^book$', book, name='book'),
    url(r'^book_list$', book_list, name='book_list'),
]
