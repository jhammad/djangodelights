import datetime
from django.db import models
from django.utils import timezone
from django.db.models import Count, F, Value

# Ingredients model
class Ingredient(models.Model):
    name = models.CharField(max_length=300)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=20)
    unit_price = models.FloatField(default=0)     
   
    def quantity_double():
        x = 5
        y = 5
        double_value = x * y
        a = Ingredient.quantity
        b = Ingredient.unit_price        
        #new_value = a * b
        #it's not working because is not mult the values but the objects itself
        return double_value
       
    
    def __str__(self):
        return self.name 
    
# Menu items model
class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField(default=0)
    
    def __str__(self):
        return self.title

# Recipes model
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, default=1, verbose_name= "menu items", on_delete=models.CASCADE)
    Ingredient = models.ForeignKey(Ingredient, default=1, verbose_name= "ingredients", on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
        
    #def __str__(self):
        #return self.menu_item 

#Purchases 
class Purchases(models.Model):
    menu_item = models.ForeignKey(MenuItem, default=1, verbose_name= "menu items", on_delete=models.CASCADE)
    Timestamp = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True, null=True)
    
    #def __str__(self):
        #return self.menu_item 



