from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("helloworldeveryone")

def greet(request,name):
    return render(request, "hello/greet.html" ,
                  {
                      "name" : name.capitalize()
                  })


def index1(request):
    return render( request , "hello/index1.html")