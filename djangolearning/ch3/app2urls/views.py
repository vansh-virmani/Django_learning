from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn(request, **kwargs): ##kwargs is passed as argument and if status keyword is given as dict in urls then ok will 
    ## else not allowed
    status=kwargs.get('status','not allowed')
    return HttpResponse(f'app 2 structure {status}')
