from django.shortcuts import render
from blog.data import posts
from django.http import Http404, HttpRequest
from typing import Any

# Create your views here.

def blog(request):
  context = {
    #"text":"olaá blog",
    "posts": posts,
    "title":"blog"
  }
  print('Blog')
  #Args= request, url , variavel
  return render(request,'blog/index.html', context)
  
def exemplo(request):
  context = {'text':'olá exemplo', 'title':'exemplo'}
  print('Exemplo')
  return render(request,'blog/exemplo.html', context)

def post(request: HttpRequest, post_id:int) -> dict[str, Any] | None:
  
  found_post = None
  
  for post in posts:
    if post['id'] == post_id:
      found_post = post
      break
  if found_post == None:
    raise Http404("Post não existe")
  context = {
    #"text":"olaá blog",
    'post': found_post,
    'title':found_post['title']
  }
  print('post', id)
  #Args= request, url , variavel
  return render(request,'blog/post.html', context,)