from django.db import models

# Create your models here.
class Product(models.Model):
	name 		= models.CharField(max_length=200)
	capacity 	= models.IntegerField(default=0)
	price 		= models.DecimalField(max_digits=10000,decimal_places=2,default=0.00)
	amount 		= models.IntegerField(default=0)
	cost 		= models.DecimalField(max_digits=10000,decimal_places=2,default=0.00)
	category 	= models.CharField(max_length=50,default='Uncategorized')
	featured 	= models.BooleanField(default=False)

	