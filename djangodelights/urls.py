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
    path("add_menut/", views.MenuCreation.as_view(), name='addmenu'),
    path("<pk>/update_menu/", views.UpdateMenu.as_view(), name='updatemenu'),
    path("<pk>/delete_menu/", views.DeleteMenu.as_view(), name='deletemenu'),


    
]