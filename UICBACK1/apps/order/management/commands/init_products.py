from django.core.management.base import BaseCommand
from faker import Faker
from apps.order.models import Product
import random

class Command(BaseCommand):
    help = "Faker yordamida Product obyektlarini yaratadi"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Yaratiladigan mahsulotlar soni')

    def handle(self, *args, **kwargs):
        fake = Faker()
        count = kwargs['count']

        for _ in range(count):
            Product.objects.create(
                name=fake.word().capitalize(),
                price=round(random.uniform(10, 1000), 2),
                is_active=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS(f"{count} ta product yaratildi."))
