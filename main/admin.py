from django.contrib import admin
from .models import (Category,
                     SubCategory,
                     Sub_SubCategory,
                     Product,
                     Brands,
                     ProductWithPrice,
                     OnlineSites,
    
)

admin.site.register(Category)
admin.site.register(Sub_SubCategory)
admin.site.register(Sub_SubCategory)
admin.site.register(OnlineSites)
admin.site.register(Product)
admin.site.register(Brands)
admin.site.register(ProductWithPrice)
