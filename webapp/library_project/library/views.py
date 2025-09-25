from django.shortcuts import render
from .models import book
# Create your views here.

def book_list(reqest):
    books = book.objects.all()
    return render(reqest, "library/book_list.html", {"books":books})


