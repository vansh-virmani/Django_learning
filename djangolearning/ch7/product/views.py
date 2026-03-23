from django.shortcuts import render
from django.http import JsonResponse

from product.models import Product
def basic(req):
    return JsonResponse({'prediction': 0.94, 'recall':0.54})

def list_(req):
    data=[' hi', 'hello','bye','success'] #for list use safe=False by default safe =True for dict only
    return JsonResponse(data,safe=False, status=201)

## view all products from model
def all_product(req):
    # Step 1: fetch only the columns you need
    queryset = Product.objects.values( 'id', 'name', 'price', 'stock')
    # queryset is still a QuerySet — not JSON serializable yet

    # Step 2: convert to plain Python list
    student_list = list(queryset)
    # now it's a normal Python list of dicts — JSON can handle this

    # Step 3: return with safe=False (it's a list)
    return JsonResponse(student_list, safe=False)

# ─── View 6: single product from DB ──────────────────────────
def single_product(request, my_id):
    product = Product.objects.get(pk=my_id)
    data = {
        'id':    product.id,
        'name':  product.name,
        'price': product.price,
        'stock': product.stock,
    }
    return JsonResponse(data)
