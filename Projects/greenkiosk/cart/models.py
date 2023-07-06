from django.db import models

# Create your models here.
class Cart(models.Model):
    name=models.CharField(max_length=10)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def subtotal(self):
        return self.quantity * self.price
    
    
    
    
    class Meta:
       verbose_name_plural = "cart"