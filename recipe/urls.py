from django.db.models.fields import related
from django.urls import path

from . import views

urlpatterns = [
    path("" , views.index, name="index")
]