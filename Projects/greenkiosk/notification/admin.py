from django.contrib import admin
from .models import Notification

class Notification_message(admin.ModelAdmin):
    list_display= ("message", "time", "is_read")

admin.site.register(Notification,Notification_message)



# Register your models here.
