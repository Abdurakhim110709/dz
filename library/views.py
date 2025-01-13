from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Book

# Create your views here.

def about_me(request):
    return HttpResponse("my name is Abdurahim")

def about_my_pet(request):
    return render(request, "about_my_pet.html")


def current_time(request):
    return HttpResponse(datetime.datetime.now())


def book_list_view(request):
    if request.method == "GET":
        book_list = Book.objects.all()
        return render(request, "books/show.html", {"book_list": book_list})

def book_detail_view(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "books/show_detail.html", {"book": book})