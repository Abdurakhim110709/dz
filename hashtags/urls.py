from django.urls import path
from . import views



urlpatterns = [
     path('tags/', views.all_products, name='all_products'),
     path('tags_male/', views.male_products, name='tag_detail'),
     path('female_tags/', views.female_products, name='all_products'),
     path('add_to_cart/<str:product_name>/<str:price>/', views.add_to_cart, name='add_to_cart'),

]
