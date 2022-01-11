from django.db import models

# Create your models here.
class Product():
	name 		= models.CharField(max_length=200)