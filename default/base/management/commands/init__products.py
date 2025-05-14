from django.core.management.base import BaseCommand
from base.models import Product
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Init products'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        count = options['count']
        products = []
        
        products = [Product(
            name=fake.word().capitalize(),
            price=round(random.uniform(10, 1000), 2)
        ) for _ in range(count)]
        products.append(products)

        Product.objects.bulk_create(products)
        # self.stdout.write(self.style.SUCCESS(f'Successfully added {count} products.'))
        print("Hello")

    def print(self):
        print('Hello')