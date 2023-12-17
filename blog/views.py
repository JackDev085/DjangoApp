from django.shortcuts import render
# Create your views here.

def blog(request):
  olha = {'text':'Olá blog',
          'title':'blog'}
  print('Blog')
  return render(request,'blog/index.html', olha)
  
def exemplo(request):
  olha = {'text':'olá exemplo', 'title':'exemplo'}
  print('Exemplo')
  return render(request,'blog/exemplo.html', olha)