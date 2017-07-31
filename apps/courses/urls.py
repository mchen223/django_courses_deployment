from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^courses/delete/(?P<id>\d+)$', views.delete_confirm),
    url(r'^courses/comment/(?P<id>\d+)$', views.add_comment),
    url(r'^comment/(?P<id>\d+)$', views.comment),
    ]
