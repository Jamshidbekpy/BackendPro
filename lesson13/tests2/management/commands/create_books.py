from django.core.management.base import BaseCommand
from faker import Faker
from tests2.models import Book, Author, Category
import random

fake = Faker()

class Command(BaseCommand):
    help = "Create fake books"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Number of books to create")

    def handle(self, *args, **options):
        count = options['count']
        authors = list(Author.objects.all())
        categories = list(Category.objects.all())

        if not authors or not categories:
            self.stdout.write(self.style.ERROR("❌ Authors or categories not found."))
            return

        books = []
        for _ in range(count):
            books.append(Book(
                title=fake.sentence(nb_words=4),
                author=random.choice(authors),
                category=random.choice(categories),
                published_date=fake.date_between(start_date='-10y', end_date='today'),
                price=round(random.uniform(10, 100), 2),
                rating=round(random.uniform(1, 5), 1),
                stock=random.randint(0, 100),
            ))

        Book.objects.bulk_create(books)
        self.stdout.write(self.style.SUCCESS(f"✅ Created {count} fake books."))
