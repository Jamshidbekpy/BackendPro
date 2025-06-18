from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from faker import Faker

class Command(BaseCommand):
    help = "Faker yordamida foydalanuvchilar yaratadi"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Yaratiladigan foydalanuvchilar soni')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        fake = Faker()
        User = get_user_model()

        for _ in range(count):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()

            user = User.objects.create_user(
                username=f"{first_name.lower()}.{last_name.lower()}{fake.random_int(1,999)}",
                email=email,
                password="password123", 
                first_name=first_name,
                last_name=last_name
            )

        self.stdout.write(self.style.SUCCESS(f"{count} ta foydalanuvchi yaratildi."))
