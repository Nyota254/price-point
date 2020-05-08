from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
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

def SubCategoryView(request, subcategory_id):
    '''
    Sub category
    Arg:
        sub-category
    '''
    title = "sub-category"
    try:
        subcategory = SubCategory.objects.get(id = subcategory_id)
    except ObjectDoesNotExist:
        raise Http404()
    
    context = {
        "subcategory":subcategory
    }
    
    return render(request,"main/subcategory.html",context)
    
    
