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

def ProductsView(request,brand_id):
    '''
    brand page
    '''
    title = "brand-page"
    try:
        products = Product.objects.get(product_brand = brand_id)
    except ObjectDoesNotExist:
        products = "Products for this category are still being populated"
        # raise Http404()
    
    
    
    context = {
        "products": products
    }
    
    return render(request,"main/products.html",context)
    
    
def ComparisonView(request,product_id):
    '''
    Comparison page for single product
    '''
    
    title = "comparison"
    
    try:
        comparisonPrices = ProductWithPrice.objects.filter(product = product_id)
    except ObjectDoesNotExist:
        raise Http404()
    
    products = Product.objects.get(id = product_id)
    
    context = {
        "comparisonPrices":comparisonPrices,
        "products":products
    }
    
    return render(request,"main/comparison.html",context)
