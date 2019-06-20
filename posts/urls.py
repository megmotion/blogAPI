from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.post_list, name="list"),
    path('create/', views.post_create),
    re_path('(?P<slug>[\w-]+)/edit/$', views.post_update, name='update'), 
    re_path('(?P<slug>[\w-]+)/delete/$', views.post_delete),
    re_path('(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),
]
