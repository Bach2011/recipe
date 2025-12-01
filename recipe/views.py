from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Ingridient, Recipe
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return HttpResponse("Hi bro!")
def recipes(request):
    if(request.method == "POST"):
        if(request.POST.get("search") == 1):
            pass
        else:
            pass
        pass
    elif(request.method == "GET"):
        pass
def recipe(request):
    pass
