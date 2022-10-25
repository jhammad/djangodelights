from .models import Ingredient, MenuItem, RecipeRequirement, Purchases
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView,ListView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import IngredientCreate, MenuItemCreate, RecipeRequirementCreate, PurchasesCreate




class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = MenuItem.objects.all()
        context["requirements"] = RecipeRequirement.objects.all()
        context["total_cost"] = round(sum([x.get_cost() for x in Purchases.objects.all()]), 6) ##the 6 means that will round to .6 digits 
        context["cost1"] = round(sum([x.cost1() for x in RecipeRequirement.objects.all()]), 6) ##the 6 means that will round to .6 digits 

        return context
    
# INGREDIENTS
    
class IngredientView(TemplateView):
    template_name = "ingredients.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context["ingredients"] = Ingredient.objects.all()        
        return context     
    
class IngredientCreation(SuccessMessageMixin,CreateView):
    template_name = "add_ingredient.html"
    form_class = IngredientCreate
    success_message= "New Ingredient created"
    
class DeleteIngredient(DeleteView):  
    model = Ingredient
    success_url ="/ingredients"    
    template_name = "delete_ingredient.html"  
    
class UpdateIngredient(UpdateView):
    model = Ingredient
    form_class= IngredientCreate
    template_name = "update_ingredient.html" 

#MENU ITEMS

class MenuView(TemplateView):
    template_name = "menu_items.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context["menuitems"] = MenuItem.objects.all()        
        return context   

class MenuCreation(SuccessMessageMixin,CreateView):
    template_name = "add_menu.html"
    form_class = MenuItemCreate
    success_message= "New Ingredient created"
    
class DeleteMenu(DeleteView):  
    model = MenuItem
    success_url ="/menu_items"    
    template_name = "delete_menu.html"  
    
class UpdateMenu(UpdateView):
    model = MenuItem
    form_class= MenuItemCreate
    template_name = "update_menu.html" 



        
        
    

