from django.db import models

# Ingredients model
class Ingredients(models.Model):
    name = models.Charfield(max lenght=30)
    quantity = models.IntegerField(default=0)
    unit = models.Charfield(max lenght=30)
    unit_price = models.IntegerField(default=0)
    
    def __str__(self):
    return self.name + " " + self.units
    
    
# Recipes (Meu items model)
class Recipe(models.Model):
    name = models.Charfield(max lenght=30)
    price = models.IntegerField(_(default=0))
    ingredients = models.ForeignKey(Ingredients, default=1, verbose_name= "Ingredients", on_delete=models.CASCADE)
    # we will delete the recipe if the ingredient is deleted 
    
    def __str__(self):
    return self.name + " " + self.units

# Clients 
class Clients(models.Model):
    name = models.Charfield(max lenght=30)
    password = models.Charfield(max lenght=30)
    client_id = models.IntegerField(default=0)
        
    def __str__(self):
    return self.name + " " + self.client_id

#Purchases 
class Purchases(models.models):
    purchase_id = models.IntegerField(default=0)
    purchase_total_price = models.IntegerField(default=0)
    client = models.ForeignKey(Clients, default=1, verbose_name= "client", on_delete=models.SET_DEFAULT)
    #We don't want to delete the purchase if the client is deleted

    def __str__(self):
    return self.purchase_id + " " + self.purchase.price + " " + self.client_name


