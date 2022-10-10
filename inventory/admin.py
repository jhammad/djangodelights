from django.contrib import admin

# Register your models here.
from django.contrib.auth.decorators import login_required
from .models import Ingredient, MenuItem, RecipeRequirement, Purchases

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)
admin.site.register(Purchases)