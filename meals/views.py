from django.shortcuts import render
from .models import Meal
from django.views import generic

# Create your views here.

class MealList(generic.ListView):
    model= Meal
    