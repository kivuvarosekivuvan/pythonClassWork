from django.db import models

class Category (models.Model):
    category_name = models.CharField(max_length=20)
    # image= models.ImageField()


    def display_category(self):
        self.category_name


    class Meta:
        verbose_name_plural = "category"

        
# Create your models here.
