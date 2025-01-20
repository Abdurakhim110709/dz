from django.views.generic import ListView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import Cart



class AllProductsView(ListView):
    model = Cart
    template_name = 'hashtags/all_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()

        search_query = self.request.GET.get('query', '')
        if search_query:
            queryset = queryset.filter(product_name__icontains=search_query)

        return queryset


class MaleProductsView(ListView):
    model = Cart
    template_name = 'hashtags/male_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Cart.objects.filter(tag__name='Male')


class FemaleProductsView(ListView):
    model = Cart
    template_name = 'hashtags/female_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Cart.objects.filter(tag__name='Female')


class CartView(ListView):
    model = Cart
    template_name = 'cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user, status='Pending')


class AddToCartView(View):
    def post(self, request, product_name, price):
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


class RemoveFromCartView(View):
    def post(self, request, cart_id):
        cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
        cart_item.delete()
        return redirect('cart')


