from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, render


from .models import Author, Book, Publisher, Store
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def store(request):
    store_list = Store.objects.prefetch_related('books').all()
    return render(request, 'annotate_aggregate/store.html', {'store_list': store_list})


def store_in(request, pk):
    books = Book.objects.select_related('publisher').prefetch_related('authors').filter(pk=pk)
    return render(request, 'annotate_aggregate/store_in.html', {'book': books})


def authors(request):
    author = Author.objects.all()
    return render(request, 'annotate_aggregate/authors.html', {'author': author})


def authors_in(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.book_set.all()
    avg = author.book_set.aggregate(a=Avg('price'))
    return render(request, 'annotate_aggregate/authors_in.html', {'books': books, 'avg': avg.get('a')})


def book(request):
    books = Book.objects.all()
    return render(request, 'annotate_aggregate/books.html', {'books': books})


def book_in(request, pk):
    books = Book.objects.select_related('publisher').prefetch_related('authors').filter(pk=pk)
    return render(request, 'annotate_aggregate/books_in.html', {'books': books})


# def publisher(request):
#     pub = Publisher.objects.annotate(a=Count('book'))
#     return render(request, 'annotate_aggregate/publisher.html', {'pub': pub})
#
#
# def publisher_in(request, pk):
#     pub = get_object_or_404(Publisher, pk=pk)
#     books = pub.book_set.all()
#     return render(request, 'annotate_aggregate/publisher_in.html', {'books': books, 'pub': pub})


class PublisherList(generic.ListView):
    model = Publisher
    paginate_by = 5
    template_name = 'annotate_aggregate/publisher_list.html'


class PublisherDetail(generic.DetailView):
    model = Publisher
    template_name = 'annotate_aggregate/publisher_detail.html'


class PublisherCreate(generic.CreateView):
    model = Publisher
    fields = ['name']
    # success_url = reverse_lazy("publishers")
    template_name = 'annotate_aggregate/publisher_create.html'

    def get_success_url(self):
        return reverse('annotate_aggregate:publisher-detail', kwargs={'pk': self.object.id})


class PublisherUpdate(generic.UpdateView):
    model = Publisher
    fields = ['name']
    template_name = 'annotate_aggregate/publisher_update.html'

    def get_success_url(self):
        return reverse('annotate_aggregate:publisher-detail', kwargs={'pk': self.object.id})


class PublisherDelete(generic.DeleteView):
    model = Publisher
    template_name = 'annotate_aggregate/publisher_delete.html'
    success_url = reverse_lazy('publisher-list')

