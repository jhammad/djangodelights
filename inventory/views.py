from django.shortcuts import render

# Create your views here.
from .models import Ingredient, MenuItem, RecipeRequirement, Purchases


from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class IngredientView(ListView):
  template_name = "home.html"
  model = Ingredient
  
  
class MenuView(ListView):
  template_name = "home.html"
  model = MenuItem