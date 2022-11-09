from django.core.management.base import BaseCommand
from annotate_aggregate.models import Author, Store, Publisher, Book

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    helps = "Create random Book, Author, Store, Publisher"

    def add_arguments(self, parser):
        parser.add_argument('some_id', nargs='?', type=int, choices=range(1, 11), help='Enter a number from 1 to 10')

    def handle(self, *args, **kwargs):
        objs_author = []
        objs_publisher = []
        objs_book = []
        objs_store = []
        total = kwargs['some_id']
        for i in range(total):
            author_name = fake.name()
            author_age = fake.pyint(min_value=30, max_value=80, step=1)
            name_publisher = fake.company()
            name_book = fake.first_name()
            pages_book = fake.pyint(min_value=150, max_value=600)
            price_book = fake.pyfloat(right_digits=2, min_value=1, max_value=10)
            rating_book = fake.pyfloat(right_digits=1, min_value=1, max_value=10)
            pubdate_book = fake.date()
            name_store = fake.catch_phrase()

            k_author = Author(
                name=author_name,
                age=author_age,
            )
            k_publisher = Publisher(
                name=name_publisher,
            )
            k_book = Book(
                name=name_book,
                pages=pages_book,
                price=price_book,
                rating=rating_book,
                pubdate=pubdate_book,
                publisher_id=fake.pyint(min_value=1, max_value=10)
            )
            k_store = Store(
                name=name_store,
            )
            objs_author.append(k_author)
            objs_publisher.append(k_publisher)
            objs_book.append(k_book)
            objs_store.append(k_store)
        Author.objects.bulk_create(objs_author)
        Publisher.objects.bulk_create(objs_publisher)
        Book.objects.bulk_create(objs_book)
        Store.objects.bulk_create(objs_store)
        self.stdout.write('Creation was successful!')
