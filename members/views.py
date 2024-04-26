from django.shortcuts import render
from django.template import loader
# Create your views here.

from django.http import HttpResponse

def members(request):
    print(request.GET)
    template = loader.get_template('block.html') 
    context = {"blog_entries":[
        {
            "title":"titulo1",
            "body":"body1"
        },
        {
            "title":"titulo2",
            "body":"body2"
        }
    ]}
    
    return HttpResponse(template.render(context=context))

def member(request,id):
    return HttpResponse("Hello world!" + str(id))
