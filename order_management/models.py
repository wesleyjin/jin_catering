from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

# Items, Menus, & Recipes

class Item(models.Model):
	item_id = models.AutoField(primary_key=True)
	item_name = models.CharField(max_length=30)
	item_type = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=38, decimal_places=2)
	size = models.CharField(max_length=64, blank=True)
	
	def __unicode__(self):
		return self.item_type + " - " + self.item_name

	def __str__(self):
		return self.__unicode__()


class Menu(models.Model):
	menu_id = models.AutoField(primary_key=True)
	menu_name = models.CharField(max_length=30)
	menu_date = models.DateField(default=date.today())
	items = models.ManyToManyField(Item)

	def __unicode__(self):
		return self.menu_name
	
	def __str__(self):
		return self.__unicode__()
	
	def get_absolute_url(self):
		return reverse("menu_detail", kwargs={"pk": self.pk})
	


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
	total_sales = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
	discount = models.DecimalField(max_digits=38, decimal_places=2, default=0.0)
	net_sales = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
	is_delivery = models.BooleanField(default=True)
	completed = models.BooleanField(default=False)
	last_updated = models.DateTimeField(auto_now=True)
	created_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-order_id"]

	def __str__(self):
		return f"Order #{self.order_id} [{self.order_date}, {self.customer}]"

	def save(self, *args, **kwargs):
		self.total_sales = self.get_total_sales
		self.net_sales = self.get_net_sales
		super().save(*args, **kwargs)

	@property
	def get_total_sales(self):
		return LineItem.objects.filter(order=self.order_id).aggregate(models.Sum('subtotal'))["subtotal__sum"]

	@property
	def get_net_sales(self):
		if self.total_sales:
			return self.total_sales - self.discount
		else:
			return - self.discount

	@property
	def get_num_items(self):
		return LineItem.objects.filter(order=self.order_id).aggregate(models.Sum('quantity'))['quantity__sum']



class LineItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField()
	subtotal = models.DecimalField(max_digits=38, decimal_places=2, null=True)
	packaging = models.ForeignKey(Packaging, on_delete=models.SET_NULL, blank=True, null=True)

	@property
	def get_subtotal(self):
		return self.item.price * self.quantity
	
	def save(self, *args, **kwargs):
		self.subtotal = self.get_subtotal
		super(LineItem, self).save(*args, **kwargs)
	
