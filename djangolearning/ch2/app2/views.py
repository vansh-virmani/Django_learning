from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fn2(request):
    data=10+10
    return HttpResponse(data)