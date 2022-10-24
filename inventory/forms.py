from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchases

class IngredientCreate(forms.ModelForm):
    class Meta:                 
        model = Ingredient
        fields = "__all__"       


class MenuItemCreate(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"
    
class RecipeRequirementCreate(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"
        
class PurchasesCreate(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = "__all__"
        
