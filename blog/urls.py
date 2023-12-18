from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
  #dinamic url
    path('post/<int:post_id>/',views.post,name='post'),
  #The route value starts with blog
    path('post/', views.blog, name='home'),
  
  #Every add route just put the next pass 
    path('exemplo/' , views.exemplo, name='exemplo')
]
