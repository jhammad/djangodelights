from audioop import mul
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
      
    def __str__(self):
        return f"{self.name} ({self.unit})"   
    
       
                  
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
    
  
        
    # def __str__(self):
    #     return self.menu_item 

#Purchases 
class Purchases(models.Model):
    menu_item = models.ForeignKey(MenuItem, default=1, verbose_name= "menu items", on_delete=models.CASCADE)
    Timestamp = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True, null=True)
    
    # def get_cost(self):
    #     #define menu items from Recipe requirements 
    #     recipe_objects = RecipeRequirement.objects.filter(menu_item=self.menu_item)
    #     #loop in Ingredients 
    #     return sum([z.Ingredient.unit_price for z in recipe_objects])



