from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model

User = get_user_model()

fake = Faker()
class Command(BaseCommand):
    help = "Create fake users. Usage: python manage.py create_fake_users <count>"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Number of fake users to create")

    def handle(self, *args, **options):
        count = options['count']
        users = []

        for _ in range(count):
            username = fake.user_name()
            email = fake.email()
            password = fake.password()

            user = User(
                username=username,
                email=email,
            )
            user.set_password(password)
            users.append(user)

        User.objects.bulk_create(users)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} fake users.'))
            
            
            
        
        
        