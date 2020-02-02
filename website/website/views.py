from django.shortcuts import render
from CMS.models import *
def index(request):
    background_image = None
    try:
        page = Page.objects.get(page=1,status=1)
        try:
            background_image = page.background_image.name.split("/")[-1]
        except:
            pass
    except:
        page = None
    data = {
        'page': page,
        'background_image': background_image,
    }
    return render(request,'index.html',data)

def about(request):
    background_image = None
    try:
        page = Page.objects.get(page=2,status=1)
        try:
            background_image = page.background_image.name.split("/")[-1]
        except:
            pass
    except:
        page = None
    data = {
        'active':'about',
        'page': page,
        'background_image': background_image,
    }
    return render(request,'about.html',data)