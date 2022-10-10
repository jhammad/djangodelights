import datetime
from django.db import models
from django.utils import timezone

# Ingredients model
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=30)
    unit_price = models.IntegerField(default=0)    

    def __str__(self):
        return self.name 
    
# Menu items model
class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

# Recipes model
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, default=1, verbose_name= "menu items", on_delete=models.SET_DEFAULT)
    Ingredient = models.ForeignKey(Ingredient, default=1, verbose_name= "ingredients", on_delete=models.SET_DEFAULT)
    quantity = models.IntegerField(default=0)
        
    #def __str__(self):
        #return self.menu_item 

#Purchases 
class Purchases(models.Model):
    menu_item = models.ForeignKey(MenuItem, default=1, verbose_name= "menu items", on_delete=models.SET_DEFAULT)
    Timestamp = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True, null=True)
    
    #def __str__(self):
        #return self.menu_item 



