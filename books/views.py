from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def book_list(request):
    query = request.GET.get('q')  # Search query
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books, 'query': query})

@login_required
def book_add(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Only staff members can add books.")

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form, 'title': 'Add Book'})

@login_required
def book_edit(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Only staff members can edit books.")
    
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form, 'title': 'Edit Book'})

@login_required
def book_delete(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("Only staff members can delete books.")
    
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')
