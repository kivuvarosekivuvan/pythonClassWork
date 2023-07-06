from django.contrib import admin 

from .models import Delivery


class Deliver_track(admin.ModelAdmin):
    list_display =["product_name", "status", "location", "expected_date", "actual_delivery_date"]

admin.site.register(Delivery, Deliver_track)




# Register your models here.