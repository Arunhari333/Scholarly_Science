from django.contrib import admin
from django.urls import path
from .import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.Profile, name='register'),
    path('detail/', views.Detail.as_view(), name='detail'),
    path('company-url/', views.company_page, name='company_page')
]
