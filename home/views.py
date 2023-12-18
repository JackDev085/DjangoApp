from django.shortcuts import render
# Create your views here.


def home(request):
    olha = {'title':'Home'}
    return render(
        request,
        'home/index.html',
        olha
        )
