from django.db import models
from django.conf import settings

from products.models import Product

	
class OrderProduct(models.Model):
	user  		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
	item 		= models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
	quantity 	= models.IntegerField(default=1)
	ordered 	= models.BooleanField(default=False)

	def __str__(self):
		return f"{self.quantity} of {self.item.name}"
		


class Order(models.Model):
	user  		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
	products 	= models.ManyToManyField(OrderProduct)
	ordered 	= models.BooleanField(default=False)

	'''def __str__(self):
					return self.user.username'''

	def get_item_name(self):
		return self.products.name