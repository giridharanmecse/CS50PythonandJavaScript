from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def giri(request):
    return HttpResponse("Hello, Giri!")

def dharani(request):
    return HttpResponse("Hello, Dharani!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name" : name.capitalize()
    })