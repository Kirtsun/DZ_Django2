from annotate_aggregate.models import Author, Publisher, Book, Store
from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    helps = "Create random users"

    def add_arguments(self, parser):
        parser.add_argument('some_id', nargs='?', type=int, choices=range(1, 11), help='Enter a number from 1 to 10 to'
                                                                                       ' create random users')

    def handle(self, *args, **kwargs):
        objs = []
        total = kwargs['some_id']
        for i in range(total):
            author_name = fake.name()
            author_age = fake.age()

            k = Author(
                name=author_name,
                age=author_age,
            )
            objs.append(k)
        Author.objects.bulk_create(objs)
        self.stdout.write('Users create with success!')
