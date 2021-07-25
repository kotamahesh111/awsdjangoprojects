from django.db import models

# Create your models here.
class ProductModel(models.Model):
    number = models.IntegerField(null=False)
    name = models.CharField(max_length=100,null=False)
    price = models.IntegerField(null=False)
    image = models.ImageField(upload_to='product_img')