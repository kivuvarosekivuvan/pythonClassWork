from django.db import models

class Rating(models.Model):
    username = models.CharField(max_length=7)
    rating_value = models.IntegerField()
    date_rated= models.DateTimeField(auto_now_add=True)
