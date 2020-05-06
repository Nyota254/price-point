from django.shortcuts import render
from .models import (Brand,
)

def Index_view(request):
    '''
    This is the function based view for the homepage
    '''
    title = "home"
    images = Brand.objects.all()
    context = {
        "title":title,
        "images":images,
    }
    
    return render(request,"main/index.html",context)
