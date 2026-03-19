from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn(request, **kwargs):
    status=kwargs.get('status','not allowed')
    return HttpResponse(f'hello world status is {status}')
