from django.urls import path
from . import views


urlpatterns = [
    path('about_me/', views.about_me, name='about_me'),
    path('about_my_pat/', views.about_my_pet, name='about_my_pet'),
    path('current_time', views.current_time, name='current_time'),

    path('books/<int:id>/', views.book_detail_view, name='book_detail'),
    path('books/', views.book_list_view, name='book_list'),
]
