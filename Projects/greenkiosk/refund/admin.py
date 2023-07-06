from django.contrib import admin

# Register your models here.
from .models import Refund


class Refund_item(admin.ModelAdmin):
    list_display =["ordered_product", "reason", "created_at", "is_approved"]

admin.site.register(Refund, Refund_item)

