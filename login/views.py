from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'home.html', {"name":"timthy" })

def register(request):
    name=request.POST('name')
    email=request.POST('email')
    password=request.POST('password')
    pass
