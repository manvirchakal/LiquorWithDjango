from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product

# Create your views here.
def homepage_view(request, *args, **kwargs):
	featured_items = Product.objects.filter(featured=True)
	length = len(featured_items)
	context = {
		'length': length,
		'featured_items': featured_items
		}

	return render(request, "index.html", context)

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})

def signup_view(request, *args, **kwargs):
	return render(request, 'signup.html', {})