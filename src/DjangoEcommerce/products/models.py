from django.db import models

# Create your models here.
class Category(models.Model):
	name 		= models.CharField(max_length=100)
	image 		= models.ImageField(null=True, blank=True, upload_to="static/images/")

	def __str__(self):
		return self.name



class Product(models.Model):
	name 		= models.CharField(max_length=200)
	capacity 	= models.IntegerField()
	price 		= models.DecimalField(max_digits=10000,decimal_places=2)
	description = models.TextField(null=True)
	amount 		= models.IntegerField()
	cost 		= models.DecimalField(max_digits=10000,decimal_places=2)
	category 	= models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
	featured 	= models.BooleanField(default=False)
	image 		= models.ImageField(null=True, blank=True, upload_to="static/images/")

	def __str__(self):
		return self.name

	

'''class OrderItem(models.Model):
	user 	= models.For'''