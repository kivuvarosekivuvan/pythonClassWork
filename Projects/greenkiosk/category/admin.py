from django.contrib import admin 

from .models import Category


class Product_category(admin.ModelAdmin):
    list_display =["category_name"]

admin.site.register(Category, Product_category)

# Register your models here.
