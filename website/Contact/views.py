from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Message

# Create your views here.
def contact(request):
    data = {
        'active':'contact',
    }
    return render(request,'contact.html',data)

def store_message(request):
    message = Message(name=request.POST['name'],email=request.POST['email'],subject=request.POST['subject'],message=request.POST['message'])
    message.save()
    return JsonResponse({'success':True})