from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Ingridient, Recipe
from django.db import IntegrityError
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


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "recipe/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "recipe/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")

        # Ensure password matches confirmation
        password = request.POST.get("password")
        confirmation = request.POST.get("confirmation")
        if password != confirmation:
            return render(request, "recipe/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "recipe/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "recipe/register.html")
def profile(request, id):
    recipe_saved = User.objects.get(id=id).saved.all()
    return render(request, "recipe/profile.html", {"recipes":recipe_saved})