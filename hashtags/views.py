from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from django.http import HttpResponseBadRequest

def all_products(request):
    if request.method == 'GET':
         products = Cart.objects.all()
         return render(request, 'hashtags/all_products.html', {'products': products})


def male_products(request):
    if request.method == 'GET':
        products = Cart.objects.filter(tag__name='Male')
        return render(request, 'hashtags/male_products.html', {'products': products})

def female_products(request):
    if request.method == 'GET':
        products = Cart.objects.filter(tag__name='Female')
        return render(request, 'hashtags/female_products.html', {'products': products})



def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user, status='Pending')
    return render(request, 'cart.html', {'cart_items': cart_items})

def add_to_cart(request, product_name, price):
    try:
        price = float(price)
    except ValueError:
        return HttpResponseBadRequest("Invalid price format")


    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product_name=product_name,
        status='Pending',
        defaults={'price': price}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    return redirect('cart')
