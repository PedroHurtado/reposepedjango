from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def members(request):
    print(request.GET)
    return HttpResponse("Hello world!")

def member(request,id):
    return HttpResponse("Hello world!" + str(id))
