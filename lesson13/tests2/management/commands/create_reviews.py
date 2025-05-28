from django.core.management.base import BaseCommand
from faker import Faker
from tests2.models import Book, Review
from django.contrib.auth import get_user_model
import random

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = "Create fake reviews"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Number of reviews to create")

    def handle(self, *args, **options):
        count = options['count']
        users = list(User.objects.all())
        books = list(Book.objects.all())

        if not users or not books:
            self.stdout.write(self.style.ERROR("❌ Users or books not found."))
            return

        reviews = []
        for _ in range(count):
            reviews.append(Review(
                book=random.choice(books),
                user=random.choice(users),
                review_text=fake.text(max_nb_chars=200),
                stars=random.randint(1, 5),
            ))

        Review.objects.bulk_create(reviews)
        self.stdout.write(self.style.SUCCESS(f"✅ Created {count} fake reviews."))
