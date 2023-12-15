from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
  #The route value starts with blog
    path('', views.blog),
  #Every add route just put the next pass 
    path('exemplo' , views.exemplo)
]
