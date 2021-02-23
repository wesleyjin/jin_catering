from django.contrib import admin

# Register your models here.
from .models import Item, Menu, Ingredient
from .models import Packaging, Recipe
from .models import Customer, Order, LineItem


# Customize site titles
admin.site.site_header = "Leslie's Catering Admin"
admin.site.site_title = "Site administration"
# admin.site.index_template = 'admin/custom_index.html'
admin.autodiscover()

# admin.site.register(Item)
# admin.site.register(Menu)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_type', 'size','price')
    list_filter = ('item_type',)
    ordering = ('-item_id',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('menu_id', 'menu_name', 'menu_date',)
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


class LineItemInline(admin.TabularInline):
    model = LineItem
    fields = ("item", "quantity", "subtotal",)
    readonly_fields = ("subtotal",)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        field = super(LineItemInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        
        if db_field.name == "item":
            print(request)
            if request is not None:
                # Only show this week's menu in line items
                # TODO: allow for changing historical orders
                field.queryset = field.queryset.filter(menu=Menu.objects.latest("menu_id"))
            else:
                field.queryset = field.queryset.none()

        return field

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     print(Menu.objects.latest("menu_id").items.all().values_list("item_id", flat=True))
    #     # print(Menu.objects.latest("menu_id").items.all().values_list("item_id", flat=True))
    #     return qs.filter(item__in=Menu.objects.latest("menu_id").items.all().values_list("item_id", flat=True))


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_date', 'customer', 'completed')
    readonly_fields = ("total_sales", "net_sales")

    inlines = [
        LineItemInline,
    ]


# class PartAdmin(admin.ModelAdmin):
#     list_display = ('part_name', 'on_equipment', 'date_installed')
#     list_filter = ['date_installed']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Packaging, PackagingAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(LineItem)