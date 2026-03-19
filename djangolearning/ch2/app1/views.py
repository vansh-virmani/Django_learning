from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('hello')
def fn1(request):
    return HttpResponse('How are you')