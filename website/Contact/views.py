from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Message

# Create your views here.
def contact(request):
    data = {
        'active':'contact',
    }
    return render(request,'contact.html',data)

def feedback(request):
    data = {
        'active':'feedback',
    }
    return render(request,'contact.html',data)

def feedbacks(request):
    try:
        feedbacks = Message.objects.filter(typ="Feedback")
    except:
        feedbacks = []
    data = {
        'active':'feedback',
        'feedbacks':feedbacks,
    }
    return render(request,'feedbacks.html',data)

def store_message(request):
    message = Message(name=request.POST['name'],email=request.POST['email'],subject=request.POST['subject'],message=request.POST['message'],typ=request.POST['typ'],purpose=request.POST['purpose'])
    message.save()
    return JsonResponse({'success':True})