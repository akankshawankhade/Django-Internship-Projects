from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
 
def cse(request):
    return HttpResponse("Welcome to Cse Page")

def etc(request):
    return HttpResponse("Welcome to ETC Page")

def mech(request):
    return HttpResponse("Welcome to Mech Page")

def civil(request):
    return HttpResponse("Welcome to C ivil Page")        
