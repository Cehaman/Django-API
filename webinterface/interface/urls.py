from django.contrib import admin
from django.urls import path, include
from interface import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('index/', views.index, name='index'),
    path('settings/', views.settings, name='settings'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)