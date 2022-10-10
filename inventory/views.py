from django.shortcuts import render

# Create your views here.
from .models import Ingredient, MenuItem, RecipeRequirement, Purchases


from django.views.generic import TemplateView, ListView


class HomeView(TemplateView):
    template_name = "home.html"

def get_context_data(self):
    context = super().get_context_data()
    context["Ingredients"] = Ingredient.objects.all()
    return context