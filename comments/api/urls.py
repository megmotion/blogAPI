from django.contrib import admin
from django.urls import path, re_path
from .views import (
	CommentCreateAPIView,
	CommentDetailAPIView,
	CommentListAPIView
	)

app_name = "comments-api" 

urlpatterns = [
    re_path('(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    path('create/', CommentCreateAPIView.as_view(), name='create'),	 
    path('', CommentListAPIView.as_view(), name='list'),
    # re_path('(?P<id>\d+)/delete/$', CommentDetailAPIView.as_view(), name='thread'),
]
