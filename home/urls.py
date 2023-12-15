from django.contrib import admin
from django.urls import path
from home import views

#Urls of app home
urlpatterns = [
  #path  -- view to render
    path('', views.home)
]
