"""DjangoEcommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import homepage_view, about_view, signup_view, cart_view, login_view
from products.views import dynamic_lookup_view
from cart.views import add_to_cart, remove_from_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name='home'),
    path('about/', about_view, name='about'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('products/<int:my_id>/', dynamic_lookup_view, name='product'),
    path('products/add-to-cart/<int:my_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('cart/products/remove-from-cart/<int:my_id>/', remove_from_cart, name='remove_from_cart'),
]
