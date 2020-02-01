from django.urls import path
from . import views

urlpatterns = [
    path('store-message',views.store_message,name="store_message"),
    path('',views.contact,name="contact"),
    path('feedback',views.feedback,name="feedback"),
    path('feedbacks',views.feedbacks,name="feedbacks"),
]
