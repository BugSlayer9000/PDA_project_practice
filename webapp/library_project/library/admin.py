from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import book

admin.site.register(book)