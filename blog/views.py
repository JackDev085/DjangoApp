from django.shortcuts import render
from blog.data import posts
# Create your views here.

def blog(request):
  context = {
    "text":"olaá blog",
    "posts": posts
  }
  print('Blog')
  #Args= request, url , variavel
  return render(request,'blog/index.html', context)
  
def exemplo(request):
  olha = {'text':'olá exemplo', 'title':'exemplo'}
  print('Exemplo')
  return render(request,'blog/exemplo.html', olha)