from django.contrib import admin
from django.urls import path,include
from myweb import views

urlpatterns = [
    path('',views.index,name='home'),
    path('projects',views.projects,name='projects'),


]
