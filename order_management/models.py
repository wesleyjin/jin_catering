from django.db import models

# Create your models here.

# Items, Menus, & Recipes

class Item(models.Model):
	item_id = models.AutoField(primary_key=True)
	item_name = models.CharField(max_length=30)
	item_type = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=38, decimal_places=2)
	size = models.CharField(max_length=10, blank=True)
	
	def __unicode__(self):
		return self.item_type + " - " + self.item_name

	def __str__(self):
		return self.__unicode__()


class Menu(models.Model):
	menu_id = models.AutoField(primary_key=True)
	menu_name = models.CharField(max_length=30)
	menu_date = models.DateField
	items = models.ManyToManyField(Item)

	def __unicode__(self):
		return self.menu_name
	
	def __str__(self):
		return self.__unicode__()		


class Ingredient(models.Model):
	ingredient_id = models.AutoField(primary_key=True)
	ingredient_name = models.CharField(max_length=100)
	ingredient_type = models.CharField(max_length=30)
	in_stock = models.IntegerField()

	def __unicode__(self):
		return '{} ({})'.format(self.ingredient_name, self.ingredient_type)

	def __str__(self):
		return self.__unicode__()


class Packaging(models.Model):
	packaging_id = models.AutoField(primary_key=True)
	packaging_type = models.CharField(max_length=30)
	size = models.CharField(max_length=10)
	in_stock = models.IntegerField()

	def __unicode__(self):
		return self.packaging_type

	def __str__(self):
		return self.__unicode__()		


class Recipe(models.Model):
	recipe_id = models.AutoField(primary_key=True)
	recipe_name = models.CharField(max_length=30)
	item = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True)
	portions = models.IntegerField()
	time_to_cook = models.DurationField(blank=True, null=True)
	directions = models.TextField(blank=True)
	ingredients = models.ManyToManyField(Ingredient)
	created_date = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.recipe_name + ' Recipe'

	def __str__(self):
		return self.__unicode__()			


class Customer(models.Model):
	customer_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=60)
	# first_name = models.CharField(max_length=30)
	# last_name = models.CharField(max_length=30)
	phone_number = models.CharField(max_length=18)
	address = models.CharField(max_length=60, blank=True)
	city = models.CharField(max_length=30, blank=True)
	notes = models.TextField(blank=True)
	created_date = models.DateField(auto_now_add=True)
	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.__unicode__()	    


class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	order_date = models.DateField()
	deliver_date = models.DateField()
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	items = models.ManyToManyField(Item,
		through='OrderItem',
		through_fields=('order', 'item'))
	total_sales = models.DecimalField(max_digits=38, decimal_places=2)
	is_delivery = models.BooleanField(blank=True, null=True)
	paid = models.BooleanField(blank=True, null=True)
	last_updated = models.DateTimeField(auto_now=True)
	created_date = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField()
	cost = models.DecimalField(max_digits=38, decimal_places=2)
	packaging = models.ForeignKey(Packaging, on_delete=models.SET_NULL, blank=True, null=True)