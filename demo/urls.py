#!/usr/bin/python
from django.conf.urls import url

from demo.views import IndexView, CompanyListView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView

app_name = 'demo'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^company_list/$', CompanyListView.as_view(), name='company_list'),
    url(r'^company_create/$', CompanyCreateView.as_view(), name='company_create'),
    url(r'^company/(?P<company_id>\d+)/$', CompanyUpdateView.as_view(), name='company_update'),
    url(r'^company/(?P<company_id>\d+)/delete/$', CompanyDeleteView.as_view(), name='company_delete'),
]
