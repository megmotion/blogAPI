from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = "comments"

urlpatterns = [
	re_path('(?P<id>\d+)/$', views.comment_thread, name='thread'),
    re_path('(?P<id>\d+)/delete/$', views.comment_delete, name='delete'),
]
