from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

#def sarayut(request):
    #return HttpResponse("Hello, Sarayut!")

#def david(request):
    #return HttpResponse("Hello, David!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

def greet2(request, name):
    return render(request, 'hello/greeting.html', 
                  {"name": name.capitalize()})