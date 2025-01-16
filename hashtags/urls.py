from django.urls import path, include
from . import views



urlpatterns = [
     path('tags/', views.all_products, name='all_products'),
     path('tags_male/', views.male_products, name='tag_detail'),
     path('female_tags/', views.female_products, name='all_products'),
]