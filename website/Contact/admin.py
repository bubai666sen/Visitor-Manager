from django.contrib import admin
from .models import *

class MessageAdmin(admin.ModelAdmin):
    #model = Message
    list_display = ['name', 'email','typ','status','subject','message']
    list_filter = ('typ', 'status')

# Register your models here.
admin.site.register(Message,MessageAdmin)
admin.site.register(SiteContact)