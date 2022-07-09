from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def efg(request):
    return HttpResponse("hello friends")
def abcd(request):
    return render(request,"abcd/abcd.html")


def first(request):
    return render(request,"abcd/first.html")

def new(request):
    return render(request,"abcd/new.html")
    
def index(request):
    return render(request,"abcd/hello.html")

def prac(request):
    return render(request,"abcd/prac4.html")

def load(request):
    return render(request,"abcd/image.html")

def ext(request):
    return render(request,"abcd/extension.html")