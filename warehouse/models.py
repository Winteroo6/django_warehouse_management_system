from django.db import models

# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Supplier(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	products_supplied = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)	

	def __str__(self):
		return self.name


class Inventory(models.Model):

	CATEGORY = ( 
			('Electronic', 'Electronic'), 
			('Furniture', 'Furniture'),
			('Clothing', 'Clothing'),
	)

	supplier = models.ForeignKey(Supplier, null=True, on_delete= models.SET_NULL)
	product = models.CharField(max_length=200, null=True)
	sku = models.CharField(max_length=200, null=True)
	price = models.CharField(max_length=200, null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True)
	location = models.CharField(max_length=200, null=True) 
	quantity = models.CharField(max_length=200, null=True) 
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.category	


class Inbound(models.Model):

	STATUS = ( 
			('Pending', 'Pending'), 
			('Out For Delivery', 'Out For Delivery'),
			('Delivered', 'Delivered'),
	)

	supplier = models.ForeignKey(Supplier, null=True, on_delete= models.SET_NULL)
	product_received = models.ForeignKey(Inventory, null=True, on_delete= models.SET_NULL)
	location = models.CharField(max_length=200, null=True) 
	quantity = models.CharField(max_length=200, null=True) 
	reference = models.CharField(max_length=200, null=True) 
	date_received = models.DateTimeField(auto_now_add=True, null=True)
	sku = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return self.status	

class Outbound(models.Model):

	STATUS = ( 
				('Pending', 'Pending'), 
				('Out For Delivery', 'Out For Delivery'),
				('Delivered', 'Delivered'),
		)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product_shipped = models.ForeignKey(Inventory, null=True, on_delete= models.SET_NULL)
	destination = models.CharField(max_length=200, null=True) 
	quantity = models.CharField(max_length=200, null=True) 
	reference = models.CharField(max_length=200, null=True) 
	date_shipped = models.DateTimeField(auto_now_add=True, null=True)
	sku = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)	

	def __str__(self):
		return self.status	