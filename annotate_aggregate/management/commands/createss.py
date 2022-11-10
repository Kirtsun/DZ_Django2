from django.core.management.base import BaseCommand
from annotate_aggregate.models import Author, Store, Publisher, Book
import random

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    helps = "Create random Book, Author, Store, Publisher"

    def add_arguments(self, parser):
        parser.add_argument('some_id', nargs='?', type=int, choices=range(1, 21), help='Enter a number from 1 to 10')

    def handle(self, *args, **kwargs):
        book_list = ["Harry Potter and the Philosopher's Stone", "Harry Potter and the Chamber of Secrets",
                     "Harry Potter and the Prisoner of Azkaban", "Lord of the Rings",
                     "Harry Potter and the Goblet of Fire", "Harry Potter and the Order of the Phoenix",
                     "Harry Potter and the Half-Blood Prince", "Harry Potter and the Deathly Hallows",
                     "The Hobbit", "It", "Doctor sleep", "Gulliver's Travels", "Nightmare Abbey", "Stormy Pass",
                     "Scarlet letter", "Alice's Adventures in Wonderland", "Moonstone", "Stolen",
                     "Portrait of Dorian Gray", "Dracula"]
        objs_author = []
        objs_publisher = []
        objs_book = []
        objs_store = []
        total = kwargs['some_id']
        for i in range(total):
            k_author = Author(
                name=fake.name(),
                age=fake.pyint(min_value=30, max_value=80, step=1),
            )
            k_publisher = Publisher(
                name=fake.company(),
            )
            k_store = Store(
                name=fake.catch_phrase(),
            )
            objs_author.append(k_author)
            objs_publisher.append(k_publisher)
            objs_store.append(k_store)
        Author.objects.bulk_create(objs_author)
        Publisher.objects.bulk_create(objs_publisher)
        Store.objects.bulk_create(objs_store)
        for b in range(total):
            k_book = Book(
                name=fake.name(),
                pages=fake.pyint(min_value=200, max_value=600),
                price=fake.pyfloat(right_digits=2, min_value=1, max_value=10),
                rating=fake.pyfloat(right_digits=1, min_value=1, max_value=10),
                pubdate=fake.date(),
                publisher_id=random.choice(Publisher.objects.values_list('id', flat=True))
            )
            objs_book.append(k_book)
        Book.objects.bulk_create(objs_book)

        self.stdout.write('Creation was successful!')
