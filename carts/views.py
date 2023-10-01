from django.shortcuts import render
from .models import Cart,CartProduct
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.decorators import login_required
from meals.models import Meal
# Create your views here.



@login_required
def cart_products(request):
    cart=Cart.objects.get(user=request.user)
    products=CartProduct.objects.filter(cart=cart)
    return render(request,'cartproduct_list.html',{'products':products})

@login_required
def add_product(request,id):
    product=Meal.objects.get(id=id)
    cart=Cart.objects.get(user=request.user)
    CartProduct.objects.create(cart=cart,product=product)
    return render(request,'add_product.html')