from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display= ("name", "stock", "price","description","date_created","date_updated")

admin.site.register(Product,ProductAdmin)

