from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_page

from .models import Author, Book, Publisher, Store


def store(request):
    store_list = Store.objects.prefetch_related('books').all()
    return render(request, 'annotate_aggregate/store.html', {'store_list': store_list})


@cache_page(10)
def store_in(request, pk):
    books = Book.objects.select_related('publisher').prefetch_related('authors').filter(pk=pk)
    return render(request, 'annotate_aggregate/store_in.html', {'book': books})


@cache_page(10)
def authors(request):
    author = Author.objects.all().annotate(num=Count('book'))
    paginator = Paginator(author, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'annotate_aggregate/authors.html', {'page_obj': page_obj})


@cache_page(10)
def authors_in(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.book_set.all()
    avg = author.book_set.aggregate(a=Avg('price'))
    return render(request, 'annotate_aggregate/authors_in.html', {'books': books, 'avg': avg.get('a')})


@method_decorator(cache_page(10), name='dispatch')
class PublisherList(generic.ListView):
    model = Publisher
    paginate_by = 5
    template_name = 'annotate_aggregate/publisher_list.html'
    queryset = Publisher.objects.annotate(num_books=Count('book'))


@method_decorator(cache_page(10), name='dispatch')
class BookList(generic.ListView):
    model = Book
    paginate_by = 100
    template_name = 'annotate_aggregate/book_list.html'


@method_decorator(cache_page(10), name='dispatch')
class PublisherDetail(generic.DetailView):
    model = Publisher
    context_object_name = 'pub_list'
    template_name = 'annotate_aggregate/publisher_detail.html'


@method_decorator(cache_page(10), name='dispatch')
class BookDetail(generic.DetailView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'annotate_aggregate/book_detail.html'


class PublisherCreate(LoginRequiredMixin, generic.CreateView):
    model = Publisher
    fields = ['name']
    template_name = 'annotate_aggregate/publisher_create.html'

    def get_success_url(self):
        return reverse('annotate_aggregate:publisher-detail', kwargs={'pk': self.object.id})


class BookCreate(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ['name', 'pages', 'rating', 'price', 'authors', 'publisher', 'pubdate']
    template_name = 'annotate_aggregate/book_create.html'

    def get_success_url(self):
        return reverse('annotate_aggregate:book-detail', kwargs={'pk': self.object.id})


class PublisherUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Publisher
    fields = ['name']
    template_name = 'annotate_aggregate/publisher_update.html'

    def get_success_url(self):
        return reverse('annotate_aggregate:publisher-detail', kwargs={'pk': self.object.id})


class BookUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Book
    fields = ['name', 'pages', 'rating', 'price', 'authors', 'publisher', 'pubdate']
    template_name = 'annotate_aggregate/book_update.html'

    def get_success_url(self):
        return reverse('annotate_aggregate:book-detail', kwargs={'pk': self.object.id})


class PublisherDelete(LoginRequiredMixin, generic.DeleteView):
    model = Publisher
    template_name = 'annotate_aggregate/publisher_delete.html'
    success_url = reverse_lazy('publisher-list')

    def get_success_url(self):
        return reverse('annotate_aggregate:publisher-list')


class BookDelete(LoginRequiredMixin, generic.DeleteView):
    model = Book
    template_name = 'annotate_aggregate/book_delete.html'
    success_url = reverse_lazy('books-list')

    def get_success_url(self):
        return reverse('annotate_aggregate:books-list')
