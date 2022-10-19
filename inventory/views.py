from .models import Ingredient, MenuItem, RecipeRequirement, Purchases

from django.views.generic import TemplateView


class IngredientView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["requirements"] = RecipeRequirement.objects.all()
        context["total_cost"] = round(sum([x.get_cost() for x in Purchases.objects.all()]), 2)
        return context
