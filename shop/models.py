from django.db import models

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length = 30)
	category = models.CharField(max_length = 30, default = "")
	subcategory = models.CharField(max_length = 30, default = "")
	desc = models.CharField(max_length = 400)
	price = models.IntegerField(default = 0)
	pub_date = models.DateField()
	image = models.ImageField(upload_to = '', default = "")

	def __str__(self):
		return self.product_name

class Contact(models.Model):
	name = models.CharField(max_length = 50, default = "")
	email = models.CharField(max_length = 50, default = "")
	phone = models.IntegerField(default = 0)
	desc = models.CharField(max_length = 500, default = "")

	def __str__(self):
		return self.name

class Order(models.Model):
	items_json = models.CharField(max_length = 5000)
	name = models.CharField(max_length = 50)
	email = models.CharField(max_length = 50)
	phone = models.CharField(max_length = 11)
	address = models.CharField(max_length = 5000)
	city = models.CharField(max_length = 50)
	state = models.CharField(max_length = 50)
	zip_code = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

class Update(models.Model):
	order_id  = models.IntegerField(default=0)
	update_desc = models.CharField(max_length = 5000)
	timestamp = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.update_desc[0:7] + '...'