from audioop import mul
import datetime
from django.db import models
from django.utils import timezone
from django.db.models import Count, F, Value
from django.urls import reverse

# Ingredients model
class Ingredient(models.Model):
    name = models.CharField(unique=True, max_length=300)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=20)
    unit_price = models.FloatField(default=0)
    
    def get_absolute_url(self):
        return ("/ingredients") ##Get an url from the name in the urls.py  
                    
    def __str__(self):
        return f"{self.name}"       
       
                  
# Menu items model
class MenuItem(models.Model):
    title = models.CharField(unique=True,max_length=30)
    price = models.FloatField(default=0) 
    
    def get_absolute_url(self):
        return ("/menu_items") ##Get an url from the name in the urls.py    
    
    def __str__(self):
        return self.title

# Recipes model   

    
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, verbose_name= "menu items", on_delete=models.CASCADE)
    Ingredient = models.ForeignKey(Ingredient, verbose_name= "ingredients", on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)      
     
    def get_absolute_url(self):
        return ("/recipes") ##Get an url from the name in the urls.py   
              
    def __str__(self):
        return f"{self.menu_item, self.Ingredient, self.quantity}" 
    
    # Function to calculate if there are enough ingredients for the recipe
    def enough(self):
        return self.quantity <= self.ingredient.quantity
    
#JaffaCake class function
class Jaffamanager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(menu_item='Jaffa Cake')

#JaffaCake class object 

    
    
    

#Purchases 
class Purchases(models.Model):
    menu_item = models.ForeignKey(MenuItem, verbose_name= "menu items", on_delete=models.CASCADE)
    quantity = models.FloatField(default=0) 
    Timestamp = models.DateTimeField(verbose_name=("Creation date"), auto_now_add=True, null=True)
    
    def get_absolute_url(self):
        return ("/purchases") ##Get an url from the name in the urls.py      
    
    def __str__(self):
        return f"{self.menu_item, self.Timestamp, self.quantity}"
    
    # def get_cost(self):
    #     #define menu items from Recipe requirements 
    #     recipe_objects = RecipeRequirement.objects.filter(menu_item=self.menu_item)
    #     #loop in Ingredients 
    #     return sum([z.Ingredient.unit_price for z in recipe_objects])

# Model only to try to find the error in the delete ingredient


