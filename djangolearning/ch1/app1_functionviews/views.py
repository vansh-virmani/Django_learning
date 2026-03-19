from django.shortcuts import render
from django.http import HttpResponse
import json

#plain text
def function1(request):
    return HttpResponse("hello this is plain text")

# html rersponse
def html(request):
    return HttpResponse("<h1>hello how u are doing</h1>")


#json response
def myjson(request):
    data = {"message": "Hello World", "status": "ok"}
    return HttpResponse(json.dumps(data),content_type='application/json')

#logic resides here
def mathlogic(request):
    data=10+10
    return HttpResponse(data)

#home url=''
def home(request):
    return HttpResponse("You are on the home page")

# Create your views here.
