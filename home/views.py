from django.shortcuts import render
# Create your views here.


def home(request):
    olha = {'text':'Um texto foda', 'title':'Home'}
    return render(
        request,
        'home/index.html',
        olha
        )
