# _*_ coding:utf-8 _*_

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^(\d+)/$',views.detail),
]