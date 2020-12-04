from django.urls import path,include
from Storage.views import *



urlpatterns = [
    path('',FileListAPIView.as_view(),name='Home'),
    path('create',FileCreateAPIView.as_view(),name='create'),
    path('<slug:slug>/update',FileUpdateAPIView.as_view(),name='update'),
    path('<slug:slug>/delete',FileDeleteAPIView.as_view(),name='delete'),
    path('<slug:slug>',FileDetailsAPIView.as_view(),name='details'),
]