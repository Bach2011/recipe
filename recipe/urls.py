from django.db.models.fields import related
from django.urls import path

from . import views

urlpatterns = [
    path("" , views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("recipe/<int:id>", views.recipe, name="recipe"),
    path("profile/<int:id>", views.profile, name="profile"),
    path("recipes", views.recipes, name="recipes"),
    path("logout", views.logout_view, name="logout"),
    path("contact", views.contact, name="contact"),
    path("collection", views.collection, name="collection"),
    path("aboutus", views.aboutus, name="aboutus")
]