from django.urls import path
from .views import AllProductsView, MaleProductsView, FemaleProductsView, CartView, AddToCartView, RemoveFromCartView

urlpatterns = [
    path('products/', AllProductsView.as_view(), name='all_products'),
    path('products/male/', MaleProductsView.as_view(), name='male_products'),
    path('products/female/', FemaleProductsView.as_view(), name='female_products'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<str:product_name>/<str:price>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
]
