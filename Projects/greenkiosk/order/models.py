from django.db import models

# Create your models here.
class Order(models.Model):
    name=models.CharField(max_length=20)
    quantity=models.PositiveIntegerField()





