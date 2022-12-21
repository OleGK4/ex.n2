from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('product', Products.as_view(), name='product'),
    path('about', About.as_view(), name='about'),
    path('contacts', Contacts.as_view(), name='contacts'),
    path('add_product', AddProduct.as_view(), name='add_product'),
    path('login', Login.as_view(), name='login'),
    path('logout', LogOut.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
