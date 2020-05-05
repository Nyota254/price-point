from django.db import models

class Category(models.Model):
    '''
    class for major categorys
    '''
    category = models.CharField(max_length=60)
    
    
class SubCategory(models.Model):
    '''
    Class for subcategory of category
    '''
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=60)
    
    
class Sub_SubCategory(models.Model):
    '''
    Class for subcategory of the sub category
    '''
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    sub_subcategory = models.CharField(max_length=60)
    

class OnlineSites(models.Model):
    '''
    Online sites
    '''
    logo = models.ImageField(upload_to='online_store_logos/')
    online_site = models.CharField(max_length=50)
    international = models.BooleanField(default=False)
    
class Brands(models.Model):
    '''
    Brands
    '''
    brand_pic = models.ImageField(upload_to='brandimage/')
    brand_name = models.CharField(max_length=50)
    
class Product(models.Model):
    '''
    product
    '''
    product_pic = models.ImageField(upload_to='product_picture/')
    product = models.CharField(max_length=60)
    product_brand = models.ForeignKey(Brands,on_delete=models.CASCADE)
    
class ProductWithPrice(models.Model):
    '''
    Product itself
    '''
    sub_subcategory = models.ForeignKey(Sub_SubCategory,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    online_site_ = models.ForeignKey(OnlineSites,on_delete=models.CASCADE)
    price = models.IntegerField()
