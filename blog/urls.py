from django.contrib import admin
from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
  #The route value starts with blog
    path('', views.blog, name='blog'),
  #Every add route just put the next pass 
    path('exemplo' , views.exemplo, name='exemplo')
]
