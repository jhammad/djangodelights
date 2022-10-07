import datetime
from django.db import models
from django.utils import timezone

# Ingredients model
class Ingredient(models.Model):
    name = models.Charfield(max lenght=30)
    quantity = models.IntegerField(default=0)
    unit = models.Charfield(max lenght=30)
    unit_price = models.IntegerField(default=0)
    
    def __str__(self):
    return self.name + " " + self.units
    
    
# Menu items model
class MenuItem(models.Model):
    title = models.Charfield(max lenght=30)
    price = models.IntegerField(_(default=0))
    
    def __str__(self):
    return self.name + " " + self.units

# Recipes model
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, default=1, verbose_name= "menu items", on_delete=models.SET_DEFAULT)
    Ingredient = models.ForeignKey(Ingredient, default=1, verbose_name= "ingredients", on_delete=models.SET_DEFAULT)
    quantity = models.IntegerField(default=0)
        
    def __str__(self):
    return self.name + " " + self.client_id

#Purchases 
class Purchases(models.models):
    menu_item = models.ForeignKey(MenuItem, default=1, verbose_name= "menu items", on_delete=models.SET_DEFAULT)
    Timestamp = models.DateTimeField(verbose_name=_("Creation date"), auto_now_add=True, null=True)
    def __str__(self):
    return self.purchase_id + " " + self.purchase.price + " " + self.client_name


