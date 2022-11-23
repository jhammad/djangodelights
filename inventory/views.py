from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from .models import Ingredient, MenuItem, RecipeRequirement, Purchases
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import IngredientCreate, MenuItemCreate, RecipeRequirementCreate, PurchasesCreate
from django.shortcuts import render, redirect
import datetime

ingredient = Ingredient.objects.all() 
menuitems = MenuItem.objects.all()
reciperequirement = RecipeRequirement.objects.all()
purchases = Purchases.objects.all()

class HomeView(LoginRequiredMixin, TemplateView):
    login_url ='login'
    template_name = "home.html"
   
# INGREDIENTS
    
class IngredientView(LoginRequiredMixin, TemplateView):
    login_url ='login'
    template_name = "ingredients.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context["ingredients"] = Ingredient.objects.all()        
        return context     
    
class IngredientCreation(SuccessMessageMixin,CreateView):
    template_name = "add_ingredient.html"
    form_class = IngredientCreate
    success_message= "New Ingredient created"
    
class DeleteIngredient(LoginRequiredMixin, DeleteView):  
    login_url ='login'
    model = Ingredient
    success_url ="/ingredients"    
    template_name = "delete_ingredient.html"  
    
class UpdateIngredient(LoginRequiredMixin, UpdateView):
    login_url ='login'
    model = Ingredient
    form_class= IngredientCreate
    template_name = "update_ingredient.html" 

#MENU ITEMS

class MenuView(LoginRequiredMixin, TemplateView):
    login_url ='login'
    template_name = "menu_items.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context["menuitems"] = MenuItem.objects.all()
        return context 
      
class MenuCreation(SuccessMessageMixin,CreateView):
    template_name = "add_menu.html"
    form_class = MenuItemCreate
    success_message= "New Ingredient created"
    
class DeleteMenu(LoginRequiredMixin, DeleteView):  
    login_url ='login'
    model = MenuItem
    success_url ="/menu_items"    
    template_name = "delete_menu.html"  
    
class UpdateMenu(LoginRequiredMixin, UpdateView):
    login_url ='login'
    model = MenuItem
    form_class= MenuItemCreate
    template_name = "update_menu.html" 

#MENU RECIPES

class RecipeView(LoginRequiredMixin, TemplateView):
    login_url ='login'
    template_name = "recipes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context["recipes"] = RecipeRequirement.objects.all()        
        return context   

class RecipeCreation(SuccessMessageMixin,CreateView):
    template_name = "add_recipe.html"
    form_class = RecipeRequirementCreate
    success_message= "New Recipe created"
    
class DeleteRecipe(LoginRequiredMixin, DeleteView):  
    login_url ='login'
    model = RecipeRequirement
    success_url ="/recipes"
    template_name = "delete_recipe.html"  
    
class UpdateRecipe(LoginRequiredMixin, UpdateView):
    login_url ='login'
    model = RecipeRequirement
    form_class= RecipeRequirementCreate
    template_name = "update_recipe.html" 
    
#PURCHASES

class PurchaseView(LoginRequiredMixin, TemplateView):
    login_url ='login'
    template_name = "purchases.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context["purchases"] = Purchases.objects.all() 
        cost = 0
        for purchase in purchases:
            cost = purchase.menu_item.cost() 
        context["cost"] = cost
        return context   

class PurchaseCreation(SuccessMessageMixin,CreateView):
    template_name = "make_purchase.html"
    form_class = PurchasesCreate
    success_message= "New Purchase created"
    
class DeletePurchase(LoginRequiredMixin, DeleteView):  
    login_url ='login'
    model = Purchases
    success_url ="/purchases"
    template_name = "delete_purchase.html"  
    
class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = 'registration/signup.html'
  
def logout_create(request):
  logout(request)
  return redirect("login")
    
# ACCOUNTING FUNCTIONS 

@login_required
def Accounting(request):
    
    # list made with all the entries of the field unit price
    cost_unit_price = [items.unit_price for items in ingredient]
    
    # list made with all the entries of the field quantity
    quantity_ingredient = [items.quantity for items in ingredient]  
    
    # Getting the costs of the ingredients in the inventory
    Inventorycost = []
    # Zip function is a inbuild python function that combine
    # the elements elements of two or more iterables
    for a,b in zip (cost_unit_price, quantity_ingredient):
        
        # append the result to our empty list
        Inventorycost.append(a*b)
        
    # Purchases sum
    Purchasecost = []
    cost_purchases= [items.menu_item.price for items in purchases]
    quantity_purchases = [items.quantity for items in purchases]  

    # Zip function is a inbuild python function that combine
    # the elements elements of two or more iterables
    for c,d in zip (cost_purchases, quantity_purchases):
        
        # append the result to our empty list
        Purchasecost.append(c*d)
        Purchasecostsum = sum(Purchasecost)
        
    # Getting the cost adn quantity of the menu items
    recipe_requirements_unit_price = [items.ingredient.unit_price for items in reciperequirement]
    recipe_requirements_quantity = [items.quantity for items in reciperequirement]

    today = datetime.datetime.today()    

    recipe_cost_1 = []
    for i1,i2 in zip (recipe_requirements_quantity, recipe_requirements_unit_price):
        recipe_cost_1.append(i1*i2)    
    
    return render (request, 'accounting.html',
     {
     #sum will add the values of the list 
     "inventorycost": sum(Inventorycost),
     "purchases_cost": Purchasecostsum,
     "today": today.strftime("%d-%b-%y"),
     "benefits" : Purchasecostsum - sum(Inventorycost)
     })




        
        
    

