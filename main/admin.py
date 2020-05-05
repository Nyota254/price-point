from django.contrib import admin
from .models import (Category,
                     SubCategory,
                     Sub_SubCategory,
                     Product,
                     Brand,
                     ProductWithPrice,
                     OnlineSite,
    
)

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Sub_SubCategory)
admin.site.register(OnlineSite)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(ProductWithPrice)
