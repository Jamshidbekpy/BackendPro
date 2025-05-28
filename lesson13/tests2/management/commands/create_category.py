from django.core.management.base import BaseCommand
from faker import Faker
from tests2.models import Category

fake = Faker()

class Command(BaseCommand):
    help = "Create fake categories"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Number of categories to create")

    def handle(self, *args, **options):
        count = options['count']
        categories = [
            Category(name=fake.word())
            for _ in range(count)
        ]
        Category.objects.bulk_create(categories)
        self.stdout.write(self.style.SUCCESS(f"✅ Created {count} fake categories."))
