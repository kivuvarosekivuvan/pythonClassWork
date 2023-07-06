from django.contrib import admin

# Register your models here.
from .models import Cart


class Cart_item(admin.ModelAdmin):
    list_display =["name", "quantity", "price"]

admin.site.register(Cart, Cart_item)
