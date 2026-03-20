from django.shortcuts import render

# Create your views here.

def coursename(req):
    price=14+10
    name='CN'
    context={
        'price':price,
        'name' :name  #the keys only must be passed as variable name in html file
    }
    return render(req,'course/django.html',context) # reference inside template folder
