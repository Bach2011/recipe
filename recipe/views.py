from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, Ingridient, Recipe
from django.db.models import Count, Q
from django.db import IntegrityError
import markdown2
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    recipes_list = []
    try:
        for i in range(1,3):
            recipes_list.append(Recipe.objects.get(id=i))
    except Recipe.DoesNotExist:
        pass
    return render(request, "recipe/landingpage.html", {
        "recipes":recipes_list
    })
def recipes(request):
    if(request.method == "POST"):
        if(request.POST.get("list") != ""):
            recipe_list_inp = request.POST.get("list").split(",")
            recipe_list = []
            for in_id in recipe_list_inp:
                try:
                    new = Ingridient.objects.get(name=in_id)
                    recipe_list.append(new)
                except Ingridient.DoesNotExist:
                    return render(request, 'recipe/landingpage.html', {"message":f'Ingredient {in_id} not found in database'})
            recipes = (
                Recipe.objects
                .annotate(match_count=Count('ingridents', filter=Q(ingridents__name__in=recipe_list)))
                .filter(match_count__gt=0)
                .order_by('-match_count')
            )
            return render(request, "recipe/collection.html", {
                "recoms":recipes,
                "search":request.POST.get("list")
            })
        else:
            return render(request, "recipe/collection.html", {
                "recipes":Recipe.objects.all()
            })
    elif(request.method == "GET"):
        return render(request, "recipe/recipes.html", {
            "recipes":Recipe.objects.all()
        })
def recipe(request, id):
    cur_recipe = Recipe.objects.get(id=id)
    if request.method == "POST":
        user = request.user
        user.saved.add(cur_recipe)
        user.save()
    saved = cur_recipe in request.user.saved.all()
    return render(request, "recipe/recipe.html", {
        "recipe" : cur_recipe,
        "ingredients":cur_recipe.ingridents.all(),
        "saved" : saved
    })


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
def contact(request):
    return render(request, "recipe/contact.html")
def aboutus(request):
    return render(request, "recipe/aboutus.html")
def collection(request):
    if request.method == "POST":
        search = request.POST.get('search')
        try:
            rec = Recipe.objects.get(name=search)
            return HttpResponseRedirect(reverse("recipe", args=[rec.id]))
        except Recipe.DoesNotExist:
            recom_list = []
            for reci in Recipe.objects.all():
                if search.lower() in reci.name.lower(): recom_list.append(reci)
            return render(request, "recipe/collection.html", {"recoms":recom_list, "search":search})
    else:
        lines = [[]]
        cnt = 0;
        for recipe in Recipe.objects.all():
            if cnt == len(lines):        # create a new sublist when needed
                lines.append([])

            if len(lines[cnt]) < 3:
                lines[cnt].append(recipe)
            else:
                cnt += 1
                lines.append([recipe])
        top = []
        count = 0
        for recipe in Recipe.objects.all():
            top.append(recipe)
            count+=1
            if(count >= 3): break
        return render(request, "recipe/collection.html", {
            "lines": lines,
            "top":top
        })