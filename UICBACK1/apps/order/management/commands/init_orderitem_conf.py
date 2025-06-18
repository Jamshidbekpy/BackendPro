from django.core.management.base import BaseCommand
from faker import Faker
from apps.order.models import OrderItem, OrderItemConfig
import random

class Command(BaseCommand):
    help = "Faker yordamida OrderItemConfig obyektlarini yaratadi"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Yaratiladigan konfiguratsiyalar soni')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        fake = Faker()

        order_items = OrderItem.objects.all()
        if not order_items.exists():
            self.stdout.write(self.style.ERROR("Hech qanday OrderItem topilmadi."))
            return

        for _ in range(count):
            OrderItemConfig.objects.create(
                order_item=random.choice(order_items),
                key=fake.word(),
                value=fake.word()
            )

        self.stdout.write(self.style.SUCCESS(f"{count} ta OrderItemConfig yaratildi."))
