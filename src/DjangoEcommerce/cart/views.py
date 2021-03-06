from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import OrderProduct, Order
from products.models import Product

def add_to_cart(request, my_id):
	print(request.user.is_authenticated)
	if request.user.is_authenticated:
		product = get_object_or_404(Product, id=my_id)
		print(product)
		order_product = OrderProduct.objects.get_or_create(user=request.user,item=product,ordered=False)
		order_check = Order.objects.filter(user=request.user,ordered=False)
		op_id = order_product[0].id

		if order_check.exists():
			order = order_check[0]

			if order.products.filter(item=product).exists():
				print(type(order_product[0].quantity))
				order_product[0].quantity += 1
				order_product[0].save()
				print("Added quantity")
				return redirect(request.META.get('HTTP_REFERER')) 

			else:
				order.products.add(op_id)
				print("Product added to cart")
				return redirect(request.META.get('HTTP_REFERER'))

		else:
			order = Order.objects.create(user=request.user)
			order.products.add(op_id)
			print("Product added to cart")
			return redirect(request.META.get('HTTP_REFERER'))

	else:
		return redirect('/signup')

def remove_from_cart(request, my_id):
	product = get_object_or_404(Product, id=my_id)
	print(product)
	order_check = Order.objects.filter(user=request.user,ordered=False)

	order = order_check[0]
	print(OrderProduct.objects.filter(item=product,user=request.user,ordered=False))

	order_product = OrderProduct.objects.get(item=product,user=request.user,ordered=False)
	order_product.delete()
	print("Item has been removed from your cart")
	return redirect(request.META.get('HTTP_REFERER'))
