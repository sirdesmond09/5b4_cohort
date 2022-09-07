from django.db import models
from django.forms import model_to_dict

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    desc = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    @property
    def product_list(self):
        return self.products.all().values()
    



class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.FloatField(max_length=255)
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    @property
    def category_detail(self):
        
        return model_to_dict(self.category, fields=['name', 'desc'])

    