from django.contrib import admin

# Register your models here.
# student/admin.py

from product.models import Product

admin.site.register(Product)