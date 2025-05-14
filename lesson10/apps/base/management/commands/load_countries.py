from django.core.management import BaseCommand
from django.core.files.base import ContentFile
from apps.base.models import Country
from pathlib import Path
import requests
import json

class Command(BaseCommand):
    help = 'Load countries'
    
    def read_json(self):
        file = Path(__file__).parent / 'countries.json'
        with open(file) as f:
            data = json.load(f)
        return data

    def handle(self, *args, **options):
        data = self.read_json()
        for item in data:
            country = Country(
                name=item['name'],
                code=item['code'],
                is_active=item['is_active'],
            )
            response = requests.get(item['img'])
            if response.status_code == 200:
                file_name = f"{item['code'].lower()}.png"
                country.img.save(file_name, ContentFile(response.content), save=False)
            country.save()

        self.stdout.write(self.style.SUCCESS('Countries loaded successfully.'))
