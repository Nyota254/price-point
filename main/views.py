from django.shortcuts import render
from .models import (Brand,
                     Category,
                     SubCategory,
                     Sub_SubCategory,
                     OnlineSite,
                     Brand,
                     Product,
                     ProductWithPrice,
)

def Index_view(request):
    '''
    This is the function based view for the homepage
    '''
    title = "home"
    categorys = Category.objects.all()
    # subcategorys = SubCategory.objects.all()
    context = {
        "title":title,
        "categorys":categorys,
    }
    
    return render(request,"main/index.html",context)
