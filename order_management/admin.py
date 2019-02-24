from django.contrib import admin

# Register your models here.
from .models import Item, Menu, Ingredient
from .models import Packaging, Recipe
from .models import Customer, Order, OrderItem

# admin.site.register(Item)
# admin.site.register(Menu)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_type', 'size','price')
    list_filter = ('item_type',)
    ordering = ('-item_id',)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu_name', )
    filter_horizontal = ('items',)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient_name', 'ingredient_type', 'in_stock')


class PackagingAdmin(admin.ModelAdmin):
    list_display = ('packaging_type', 'size', 'in_stock')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'portions', 'time_to_cook', 'created_date')
    filter_horizontal = ('ingredients', )


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'city', 'address')
    list_filter = ('city', )




# class PartAdmin(admin.ModelAdmin):
#     list_display = ('part_name', 'on_equipment', 'date_installed')
#     list_filter = ['date_installed']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Packaging, PackagingAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)