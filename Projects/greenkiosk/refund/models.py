from django.db import models

# Create your models here.
class Refund(models.Model):
    ordered_product = models.CharField(max_length=20)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
