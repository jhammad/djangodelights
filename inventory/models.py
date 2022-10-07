from django.db import models

# Ingredients model
class Ingredients(models.Model):
    name = models.Charfield(max lenght=30)
    units = models.IntegerField(_(default=0))
    price = models.IntegerField(_(default=0))
    
    def __str__(self):
    return self.name + " " + self.units
    
    
# Recipes (Meu items model)
class Recipe(models.Model):
    name = models.Charfield(max lenght=30)
    price = models.IntegerField(_(default=0))
    ingredients = models.Charfield(max lenght=30)
    
    def __str__(self):
    return self.name + " " + self.units

# Clients 
class Clients(models.Model):
    name = models.Charfield(max lenght=30)
    client_id = models.IntegerField(default=0)
        
    def __str__(self):
    return self.name + " " + self.client_id

#Purchases 
class Purchases(models.models):
    purchase_id = models.IntegerField(default=0)
    purchase_price = models.IntegerField(default=0)
    client_name = models.Charfield(max lenght=30)

    def __str__(self):
    return self.purchase_id + " " + self.purchase.price + " " + self.client_name


