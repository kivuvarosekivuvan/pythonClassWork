from django.contrib import admin


from .models import Order

class Order_items(admin.ModelAdmin):
    list_display =["name", "quantity"]

admin.site.register(Order, Order_items)
