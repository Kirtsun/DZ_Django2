import random

from django.core.management.base import BaseCommand
from annotate_aggregate.models import Author, Store, Book

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = "Create random connections"

    def add_arguments(self, parser):
        parser.add_argument('id', nargs='?', type=int, help="To create random connections in the database,"
                                                            " enter 'connections'")

    def handle(self, *args, **kwargs):
        if Store.objects.all().count() and Book.objects.all().count():
            id_book = Book.objects.values_list('id', flat=True)
            id_author = Author.objects.values_list('id', flat=True)
            for i in Store.objects.values_list('id', flat=True):
                q = Store.objects.get(pk=i)
                q.books.add(random.choice(id_book))
            for i in Book.objects.values_list('id', flat=True):
                q = Book.objects.get(pk=i)
                q.authors.add(random.choice(id_author))
            self.stdout.write('Connections create with success!')
        else:
            self.stdout.write('The base is empty! Fill the base with the "createss" command!!')
