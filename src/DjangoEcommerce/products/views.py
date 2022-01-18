from django.shortcuts import render

# Create your views here.
from .models import Product

def dynamic_lookup_view(request, my_id):
	product = Product.objects.get(id=my_id)
	context = {
		"product": product
	}
	return render(request, "products/product_detail.html", context)