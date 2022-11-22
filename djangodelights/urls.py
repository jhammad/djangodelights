"""djangodelights URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory import views



urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.HomeView.as_view(), name='home'),
    path("ingredients/", views.IngredientView.as_view(), name='ingredients'),
    path("add_ingredient/", views.IngredientCreation.as_view(), name='addingredient'),
    path("<pk>/delete_ingredient/", views.DeleteIngredient.as_view(), name='deleteingredient'),
    path("<pk>/update_ingredient/", views.UpdateIngredient.as_view(), name='updateingredient'),
    path("menu_items/", views.MenuView.as_view(), name='menuitems'),
    path("add_menu/", views.MenuCreation.as_view(), name='addmenu'),
    path("<pk>/update_menu/", views.UpdateMenu.as_view(), name='updatemenu'),
    path("<pk>/delete_menu/", views.DeleteMenu.as_view(), name='deletemenu'),
    path("recipes/", views.RecipeView.as_view(), name='recipes'),
    path("add_recipe/", views.RecipeCreation.as_view(), name='addrecipe'),
    path("<pk>/delete_recipe/", views.DeleteRecipe.as_view(), name='deleterecipe'),
    path("<pk>/update_recipe/", views.UpdateRecipe.as_view(), name='updaterecipe'),  
    path("purchases/", views.PurchaseView.as_view(), name='purchases'),
    path("make_purchase/", views.PurchaseCreation.as_view(), name='makepurchase'),
    path("<pk>/delete_purchase/", views.DeletePurchase.as_view(), name='deletepurchase'),
    path("accounting/", views.Accounting, name='accounting'),
    path("accounts/login/", views.Login.as_view(), name="login"),
    path("accounts/signup/", views.SignUp.as_view(), name="signup"),
]