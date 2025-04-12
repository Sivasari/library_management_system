from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Transaction
from .forms import BorrowForm
from books.models import Book
from django.contrib import messages


@login_required
def borrow_book(request):
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            # Create transaction
            Transaction.objects.create(user=request.user, book=book)
            # Reduce book copy count
            book.copies_available -= 1
            book.save()
            return redirect('my_transactions')
    else:
        form = BorrowForm()
    return render(request, 'transactions/borrow_book.html', {'form': form})


@login_required
def my_transactions(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transactions/my_transactions.html', {'transactions': transactions})


@login_required
def transactions_list(request):
    if request.user.is_staff:  # Only staff can view all
        transactions = Transaction.objects.all().order_by('-borrow_date')
    else:
        transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transactions/transactions_list.html', {'transactions': transactions})


@login_required
def return_book(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    if not request.user.is_staff:
        messages.error(request, "You are not permitted to update this status.")
        return redirect('transactions_list')  # ✅ Matches your urls.py

    if not transaction.return_date:
        transaction.return_date = timezone.now()
        transaction.save()
        messages.success(request, "Book returned successfully.")
    else:
        messages.warning(request, "This book has already been returned.")

    return redirect('transactions_list')  # ✅ This name should match your URL pattern
