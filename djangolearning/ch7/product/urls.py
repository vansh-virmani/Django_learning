# student/urls.py
from django.urls import path
from product import views

urlpatterns = [
    path('basic/',            views.basic,     name='basic_json'),
    path('list/',             views.list_,      name='list_json'),
  
    path('products/',         views.all_product,   name='all_products'),
    path('products/<int:my_id>', views.single_product, name='single_product'), #this my_id must be same as vies parameter
]