from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Ingridient(models.Model):
    name = models.CharField()
class Recipe(models.Model):
    name = models.CharField()
    picture = models.CharField(default = "")
    ingridents = models.ManyToManyField(Ingridient, related_name="food")
    description = models.CharField(default = "")
    instruction = models.CharField(default = "")
class User(AbstractUser, models.Model):
    def __str__(self):
        return f'{self.username}'
    saved = models.ManyToManyField(Recipe, related_name="sigma")