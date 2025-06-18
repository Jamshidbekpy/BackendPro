from django.core.management.base import BaseCommand
from faker import Faker
from apps.order.models import Order
from django.contrib.auth import get_user_model
import random

User = get_user_model()

class Command(BaseCommand):
    help = "Faker yordamida Order obyektlarini yaratadi"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Yaratiladigan orderlar soni')

    def handle(self, *args, **kwargs):
        fake = Faker()
        count = kwargs['count']
        users = User.objects.all()

        if not users.exists():
            self.stdout.write(self.style.ERROR("Hech qanday foydalanuvchi topilmadi."))
            return

        for _ in range(count):
            Order.objects.create(
                name=fake.name(),
                user=random.choice(users)
            )

        self.stdout.write(self.style.SUCCESS(f"{count} ta order yaratildi."))
