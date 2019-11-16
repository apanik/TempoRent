from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('products/', productview, name="products"),
    path('addproducts/', addproducts, name ="addproducts"),
    path('products/<int:id>/', productdetails, name='productdetails'),


]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

