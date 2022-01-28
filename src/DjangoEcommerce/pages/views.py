from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import Product, Category, Capacity
from cart.models import OrderProduct, Order
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def homepage_view(request, *args, **kwargs):
	#print(request.user)
	if request.user.is_authenticated:
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

	else:
		featured_items = Product.objects.filter(featured=True)
		categories = Category.objects.all()
		length = 0

		context = {
			'length': length,
			'featured_items': featured_items,
			'categories': categories,
		}

	return render(request, "index.html", context)

def about_view(request, *args, **kwargs):
	return render(request, "about.html", {})

def cart_view(request, *args, **kwargs):
	if request.user.is_authenticated:
		order_check = Order.objects.filter(user=request.user,ordered=False)
		no_order = ""
		order_items = order_check[0].products.all()
		order_total = 0
		for item in order_items:
			order_total += item.item.price*item.quantity

		order_tax = float(order_total)*0.0825
		order_tax = '%.2f'%order_tax

		order_total_tax = float(order_total) + float(order_tax)
		order_total_tax = '%.2f'%order_total_tax

		if order_check.exists():
			order = order_check
			order_items = order_check[0].products.all()

		else:
			no_order = "no items to display"

		context = {
			'order_total': order_total,
			'order_tax': order_tax,
			'order_total_tax': order_total_tax,
			'no_order': no_order,
			'order': order,
			'order_items': order_items,
		}

		return render(request, 'cart.html', context)

	else:
		return redirect('/signup')