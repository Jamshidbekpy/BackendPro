from django.core.management.base import BaseCommand
from faker import Faker
from tests.models import Order, Product, OrderItem
import random

fake = Faker()

class Command(BaseCommand):
    help = "Create fake order items"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Number of fake order items to create")

    def handle(self, *args, **options):
        count = options['count']
        orders = list(Order.objects.all())
        products = list(Product.objects.all())

        if not orders:
            self.stdout.write(self.style.ERROR("No orders found. Please create orders first."))
            return
        if not products:
            self.stdout.write(self.style.ERROR("No products found. Please create products first."))
            return

        order_items = []

        for _ in range(count):
            order = random.choice(orders)
            product = random.choice(products)
            quantity = random.randint(1, 10)

            order_item = OrderItem(
                order=order,
                product=product,
                quantity=quantity
            )
            order_items.append(order_item)

        OrderItem.objects.bulk_create(order_items)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} order items.'))
