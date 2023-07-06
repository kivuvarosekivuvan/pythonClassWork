from django.db import models

class Delivery(models.Model):
    product_name=models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=(
        ('PENDING', 'Pending'),
        ('SHIPPED', 'Shipped'),
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ))
    location = models.CharField(max_length=100)
    expected_date = models.DateField()
    actual_delivery_date = models.DateField(null=True, blank=True)
