from django.db import models
from django.forms import ModelForm




class Catagory(models.Model):
    catagory_name = models.CharField(max_length=250)


    def __str__(self):
        return self.catagory_name


class Product(models.Model):
    product_name      = models.CharField(max_length=250,null=False,blank=False)
    product_rate      = models.PositiveIntegerField(null=False,blank=False)
    product_date      = models.DateField(auto_now_add=True,null=False,blank=False)
    product_image     = models.ImageField(upload_to='products/',null=False,blank=False)
    product_rules     = models.TextField(null=False,blank=False)
    product_catagory  = models.ForeignKey(Catagory,on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self):
        return self.product_name



