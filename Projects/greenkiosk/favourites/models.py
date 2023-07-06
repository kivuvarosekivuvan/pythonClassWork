from django.db import models


class Favourites(models.Model):
    product_name = models.CharField(max_length=20)
    product_category=models.CharField(max_length=20)

    def __str__(self):
        return self.product_name
