from django.urls import path
from .views import AboutMeView, AboutMyPetView, CurrentTimeView, BookListView, BookDetailView, book_list

urlpatterns = [
    path('about-me/', AboutMeView.as_view(), name='about_me'),
    path('about-my-pet/', AboutMyPetView.as_view(), name='about_my_pet'),
    path('current-time/', CurrentTimeView.as_view(), name='current_time'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('pars_book/', book_list, name='pars_book'),
]

