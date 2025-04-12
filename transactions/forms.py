from django import forms
from .models import Transaction
from books.models import Book

class BorrowForm(forms.Form):
    book = forms.ModelChoiceField(queryset=Book.objects.filter(copies_available__gt=0))
