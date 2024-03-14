from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("helloworldeveryone")

def error_404(request, exception):
    print(hh)
    return render(request, 'templates/505_404.html', status=404)

def error_500(request):
    return render(request, 'templates/505_404.html', status=500)

def greet(request,name):
    return render(request, "hello/greet.html" ,
                  {
                      "name" : name.capitalize()
                  })


def index1(request):
    return render( request , "hello/index1.html")
