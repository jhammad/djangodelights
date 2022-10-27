from termios import OFDEL
from .models import Ingredient, MenuItem, RecipeRequirement, Purchases
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView,ListView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import IngredientCreate, MenuItemCreate, RecipeRequirementCreate, PurchasesCreate
from django.shortcuts import render




class HomeView(TemplateView):
    template_name = "home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["menu_items"] = MenuItem.objects.all()
    #     context["requirements"] = RecipeRequirement.objects.all()
    #     context["total_cost"] = round(sum([x.get_cost() for x in Purchases.objects.all()]), 6) ##the 6 means that will round to .6 digits 
    #     context["cost1"] = round(sum([x.cost1() for x in RecipeRequirement.objects.all()]), 6) ##the 6 means that will round to .6 digits 

    #     return context
    
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

#MENU RECIPES

class RecipeView(TemplateView):
    template_name = "recipes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context["recipes"] = RecipeRequirement.objects.all()        
        return context   

class RecipeCreation(SuccessMessageMixin,CreateView):
    template_name = "add_recipe.html"
    form_class = RecipeRequirementCreate
    success_message= "New Recipe created"
    
class DeleteRecipe(DeleteView):  
    model = RecipeRequirement
    success_url ="/recipes"
    template_name = "delete_recipe.html"  
    
class UpdateRecipe(UpdateView):
    model = RecipeRequirement
    form_class= RecipeRequirementCreate
    template_name = "update_recipe.html" 
    
#PURCHASES

class PurchaseView(TemplateView):
    template_name = "purchases.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context["purchases"] = Purchases.objects.all()        
        return context   

class PurchaseCreation(SuccessMessageMixin,CreateView):
    template_name = "make_purchase.html"
    form_class = PurchasesCreate
    success_message= "New Purchase created"
    
class DeletePurchase(DeleteView):  
    model = Purchases
    success_url ="/purchases"
    template_name = "delete_purchase.html"  
    
# ACCOUNTING FUNCTIONS 

def Accounting(request):
    # Object all inbuild function will grab all the fields from the models
    ingredient = Ingredient.objects.all() 
    menuitems = MenuItem.objects.all()
    reciperequirement = RecipeRequirement.objects.filter()
    
    # list made with all the entries of the field unit price
    cost_unit_price = [items.unit_price for items in ingredient]
    
    # list made with all the entries of the field quantity
    quantity_ingredient = [items.quantity for items in ingredient]  
    
    # Getting the costs of the ingredients in the inventory
    Inventorycost = []
    # Zip function is a inbuild python function that combine
    # the elements elements of two or more iterables
    for i1,i2 in zip (cost_unit_price, quantity_ingredient):
        
        # append the result to our empty list
        Inventorycost.append(i1*i2)
        
    # Getting the coxst of the menu items
    menu_items = [items.title for items in menuitems]
    recipe_requirements = [items.menu_item for items in reciperequirement.filter(quantity = 2)]
    
   
    
    return render (request, 'accounting.html',
     {
     'cost2': cost_unit_price,
     'cost3': quantity_ingredient,  
     #sum will add the values of the list 
     'inventorycost': sum(Inventorycost),
     "menu_items": menu_items,
     "recipe_requirements": recipe_requirements
     })




        
        
    

