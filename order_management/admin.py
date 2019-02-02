from django.contrib import admin

# Register your models here.
from .models import Item, Menu, Ingredient
from .models import Packaging, Recipe, RecipeIngredient
from .models import Customer, Order, OrderItem

admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(Ingredient)
admin.site.register(Packaging)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)