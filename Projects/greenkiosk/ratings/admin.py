from django.contrib import admin

from .models import Rating
# Register your models here.
class Rating_details(admin.ModelAdmin):
    list_display = ("username","rating_value","date_rated")

admin.site.register(Rating,Rating_details)
