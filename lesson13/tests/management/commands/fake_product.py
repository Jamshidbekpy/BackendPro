from django.core.management.base import BaseCommand
from faker import Faker
from tests.models import Product

fake = Faker()

class Command(BaseCommand):
    help = "Create fake products"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Number of fake products to create")

    def handle(self, *args, **options):
        count = options['count']
        products = []

        for _ in range(count):
            product = Product(
                name=fake.word().capitalize(),
                price=round(fake.pydecimal(left_digits=4, right_digits=2, positive=True), 2)
            )
            products.append(product)

        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} products.'))
