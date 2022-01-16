from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product, Category, Capacity

# Create your views here.
def homepage_view(request, *args, **kwargs):
	featured_items = Product.objects.filter(featured=True)
	categories = Category.objects.all()
	#capacities = Capacity.objects.all()
	length = len(featured_items)
	context = {
		'length': length,
		'featured_items': featured_items,
		'categories': categories,
		#'capacities': capacities
		}

	return render(request, "index.html", context)

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})

def signup_view(request, *args, **kwargs):
	return render(request, 'signup.html', {})