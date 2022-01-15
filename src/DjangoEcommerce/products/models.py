from django.db import models

# Create your models here.
class Product(models.Model):
	name 		= models.CharField(max_length=200)
	capacity 	= models.IntegerField()
	price 		= models.DecimalField(max_digits=10000,decimal_places=2)
	amount 		= models.IntegerField()
	cost 		= models.DecimalField(max_digits=10000,decimal_places=2)
	category 	= models.CharField(max_length=50,default='Uncategorized')
	featured 	= models.BooleanField(default=False)
	image 		= models.ImageField(null=True, blank=True, upload_to="static/images/")
	