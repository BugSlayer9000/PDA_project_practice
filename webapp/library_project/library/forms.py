from django import forms 
from .models import book

class BookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ["title","author","year"]

# this gives me a form based directyl on your model