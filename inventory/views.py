from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

from models import Ingredients, MenuItem, RecipeRequirement, Purchases

@login_required(login_url='login')
def dashboard(request):
    total_ingredients = Ingredients.objects.count()
 

    return render(request, 'dashboard.html', context)