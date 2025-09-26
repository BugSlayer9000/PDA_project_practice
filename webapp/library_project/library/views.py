from django.shortcuts import render, redirect
from .models import book
from .forms import BookForm
# Create your views here.

def book_list(reqest):
    books = book.objects.all()
    return render(reqest, "library/book_list.html", {"books":books})


# add a view for adding book

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "library/add_book.html",{"form":form})
            


