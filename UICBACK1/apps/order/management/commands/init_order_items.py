from django.core.management.base import BaseCommand
from faker import Faker
from apps.order.models import OrderItem, Order, Product
import random

class Command(BaseCommand):
    help = "Faker yordamida OrderItem obyektlarini yaratadi"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Yaratiladigan order itemlar soni')

    def handle(self, *args, **kwargs):
        fake = Faker()
        count = kwargs['count']
        orders = Order.objects.all()
        products = Product.objects.filter(is_active=True)

        if not orders.exists() or not products.exists():
            self.stdout.write(self.style.ERROR("Order yoki Product mavjud emas."))
            return

        for _ in range(count):
            OrderItem.objects.create(
                order=random.choice(orders),
                product=random.choice(products),
                quantity=random.randint(1, 10)
            )

        self.stdout.write(self.style.SUCCESS(f"{count} ta order item yaratildi."))
