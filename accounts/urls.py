from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.Profile, name='register'),
    path('detail/', views.Detail.as_view(), name='detail')
]
