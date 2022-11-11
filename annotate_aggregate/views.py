from django.shortcuts import get_object_or_404, render

from .models import Author, Publisher, Book, Store


def index(request):
    store_list = Store.objects.all()
    return render(request, 'annotate_aggregate/index.html', {'store_list': store_list})


def store_book(request, pk):
    book_store = Store.objects.prefetch_related('books').filter(pk=pk)
    return render(request, 'annotate_aggregate/store.html', {'book_store': book_store})


def book(request, pk):
    books = Book.objects.select_related('publisher').prefetch_related('authors').filter(pk=pk)
    return render(request, 'annotate_aggregate/book.html', {'books': books})


def publisher(request, pk):
    publish = get_object_or_404(Publisher, pk=pk)
    books = publish.book_set.all()
    return render(request, 'annotate_aggregate/publisher.html', {'publish': publish, 'books': books})


def author(request, pk):
    authors = get_object_or_404(Author, pk=pk)
    books = authors.book_set.all()
    return render(request, 'annotate_aggregate/authors.html', {'books': books, 'authors': authors})
