from django.shortcuts import render

def index(request):

    return render(request,'index.html')

def about(request):
    data = {
        'active':'about',
    }
    return render(request,'about.html',data)