from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Book
import datetime


class AboutMeView(View):
    def get(self, request):
        return HttpResponse("my name is Abdurahim")


class AboutMyPetView(View):
    def get(self, request):
        return render(request, "about_my_pet.html")


class CurrentTimeView(View):
    def get(self, request):
        return HttpResponse(datetime.datetime.now())


class BookListView(ListView):
    model = Book
    template_name = "books/show.html"
    context_object_name = "book_list"


class BookDetailView(DetailView):
    model = Book
    template_name = "books/show_detail.html"
    context_object_name = "book"
