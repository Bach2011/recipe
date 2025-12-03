from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Ingridient, Recipe
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request, "recipe/landingpage.html")
def recipes(request):
    if(request.method == "POST"):
        if(request.POST.get("search") == 1):
            recipe_list_inp = request.POST.get("list").split(",")
            recipe_list = []
            for in_id in recipe_list_inp:
                recipe_list.append(Ingridient.objects.get(id=in_id))
            
            pass
        else:
            pass
        pass
    elif(request.method == "GET"):
        pass
def recipe(request):
    pass
