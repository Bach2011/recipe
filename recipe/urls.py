from django.db.models.fields import related
from django.urls import path

from . import views

urlpatterns = [
    path("" , views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("recipe/<int:id>", views.recipe, name="recipe"),
    path("profile/<int:id>", views.profile, name="profile")
]