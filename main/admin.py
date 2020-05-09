from django.contrib import admin
from .models import (Category,
                     SubCategory,
                     Sub_SubCategory,
                     Product,
                     Brand,
                     ProductWithPrice,
                     OnlineSite,
    
)

class BrandAdmin(admin.ModelAdmin):
    filter_horizontal = ('sub_subcategory',)

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Sub_SubCategory)
admin.site.register(OnlineSite)
admin.site.register(Product)
admin.site.register(Brand,BrandAdmin)
admin.site.register(ProductWithPrice)
