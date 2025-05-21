from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model
from tests.models import Order
import random

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = "Create fake orders"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Number of fake orders to create")

    def handle(self, *args, **options):
        count = options['count']
        users = list(User.objects.all())

        if not users:
            self.stdout.write(self.style.ERROR("No users found in database. Please create users first."))
            return

        orders = []

        for _ in range(count):
            user = random.choice(users)
            order = Order(user=user)
            orders.append(order)

        Order.objects.bulk_create(orders)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} orders.'))
