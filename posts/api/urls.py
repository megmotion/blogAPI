from django.contrib import admin
from django.urls import path, re_path
from .views import (
	PostCreateAPIView,
	PostListAPIView, 
	PostDeleteAPIView, 
	PostDetailAPIView, 
	PostUpdateAPIView
	)

app_name = "posts-api"

urlpatterns = [
    path('', PostListAPIView.as_view(), name="list"),
    path('create/', PostCreateAPIView.as_view(), name="create"),
    re_path('(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'), 
    re_path('(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
    re_path('(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
    ]