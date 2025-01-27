from django.urls import path
from . import views

urlpatterns = [
    path('GoodRead_list/', views.GoodReadListView.as_view(), name='rezka_list'),
    path('GoodRead_form/', views.GoodReadFormView.as_view(), name='rezka_form'),
]