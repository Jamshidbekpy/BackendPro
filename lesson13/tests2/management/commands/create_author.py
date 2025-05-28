from django.core.management.base import BaseCommand
from faker import Faker
from tests2.models import Author
import random

fake = Faker()

class Command(BaseCommand):
    help = "Create fake authors"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Number of authors to create")

    def handle(self, *args, **options):
        count = options['count']
        authors = [
            Author(name=fake.name(), birth_date=fake.date_of_birth())
            for _ in range(count)
        ]
        Author.objects.bulk_create(authors)
        self.stdout.write(self.style.SUCCESS(f"✅ Created {count} fake authors."))
