from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    #model = Message
    list_display = ['name', 'email','subject']

# Register your models here.
admin.site.register(Message,MessageAdmin)