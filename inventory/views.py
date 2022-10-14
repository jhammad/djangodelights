from django.shortcuts import render
from django.db.models import Sum, F, FloatField, Max
from django.db.models.functions import Cast


from .models import Ingredient, MenuItem, RecipeRequirement, Purchases


from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class IngredientView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["requirements"] = RecipeRequirement.objects.all()
        context["total_cost"] = round(sum([p.get_cost() for p in Purchases.objects.all()]), 2),    
        return context 
    

