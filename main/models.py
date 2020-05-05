from django.db import models

class Category(models.Model):
    '''
    class for major categorys
    '''
    category = models.CharField(max_length=60)
    
    def __str__(self):
        return f'{self.category} Main'
    
    
class SubCategory(models.Model):
    '''
    Class for subcategory of category
    '''
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=60)
    
    def __str__(self):
        return f'{self.subcategory} of {self.category.category}'
    
    
class Sub_SubCategory(models.Model):
    '''
    Class for subcategory of the sub category
    '''
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    sub_subcategory = models.CharField(max_length=60)
    
    def __str__(self):
        return f'{self.sub_subcategory} of {self.subcategory.subcategory} of {self.subcategory.category.category}'
    

class OnlineSite(models.Model):
    '''
    Online sites
    '''
    logo = models.ImageField(upload_to='online_store_logos/')
    online_site = models.CharField(max_length=50)
    international = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.online_site } site info'
    
class Brand(models.Model):
    '''
    Brands
    '''
    brand_pic = models.ImageField(upload_to='brandimage/')
    brand_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.brand_name} info'
    
class Product(models.Model):
    '''
    product
    '''
    product_pic = models.ImageField(upload_to='product_picture/')
    product = models.CharField(max_length=60)
    product_brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.product} info'
    
class ProductWithPrice(models.Model):
    '''
    Product itself
    '''
    sub_subcategory = models.ForeignKey(Sub_SubCategory,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    online_site = models.ForeignKey(OnlineSite,on_delete=models.CASCADE)
    price = models.IntegerField()
    
    def __str__(self):
        return f'{self.product.product} Price from {self.online_site.online_site}'
