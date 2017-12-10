from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.study_list, name='study_list'),
    url(r'^(?P<id>\d+)/$', views.study_detail, name='study_detail'),
    url(r'^new/$', views.study_new),
]
