from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (Index_view,
                    SubCategoryView,
                    ProductsView,
                    ComparisonView,
)

urlpatterns = [
    path('',Index_view,name='index'),
    path('subcategory/<int:subcategory_id>/',SubCategoryView,name='subcategory'),
    path('products/<int:brand_id>/',ProductsView,name='products'),
    path('comparison/<int:product_id>/',ComparisonView,name='comparison'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)