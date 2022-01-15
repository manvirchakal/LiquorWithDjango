from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product

# Create your views here.
def homepage_view(request, *args, **kwargs):
	featured_items = Product.objects.filter(featured=True)
	count = 1
	context = {'featured_items': featured_items}

	return render(request, "index.html", context)