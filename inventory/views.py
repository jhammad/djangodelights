from django.shortcuts import render
from django.db.models import Sum, F


from .models import Ingredient, MenuItem, RecipeRequirement, Purchases


from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class IngredientView(ListView):
  template_name = "ingredients.html"
  model = Ingredient
  new_value = 2*2

  
class RecipeRequirement(ListView):
  template_name = "home.html"
  model = RecipeRequirement

