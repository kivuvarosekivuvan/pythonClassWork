from django.contrib import admin

from .models import Favourites

class Favourite_item(admin.ModelAdmin):
    list_display = ("product_name", "product_category")

admin.site.register(Favourites,Favourite_item)
# Register your models here.

