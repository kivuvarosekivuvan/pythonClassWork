from django.db import models


class Notification(models.Model):
    message = models.CharField(max_length=255)
    time= models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
# Create your models here.
