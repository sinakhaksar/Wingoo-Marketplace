from django.db import models
from django.contrib.auth.models import User




# Create your models here.
                            # Ok 

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name 
    

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=False)
    item_profile = models.ImageField(upload_to='item_images', blank=False, null=False)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name 

