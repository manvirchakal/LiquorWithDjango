from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product, Category, Capacity
from cart.models import OrderProduct, Order

# Create your views here.
def homepage_view(request, *args, **kwargs):
	#print(request.user)
	order = Order.objects.filter(user=request.user, ordered=False)
	#print(cart[0].products)
	order_items = order[0].products.all()
	#print(type(order_items[0]))
	'''print(order_items)
				items = order_items[0].item
				print(items)'''
	featured_items = Product.objects.filter(featured=True)
	categories = Category.objects.all()
	#capacities = Capacity.objects.all()
	length = len(order_items)
	context = {
		'order_items': order_items,
		'order': order,
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