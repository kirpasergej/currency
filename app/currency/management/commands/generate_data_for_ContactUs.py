from faker import Faker
from django.core.management.base import BaseCommand
from currency.models import ContactUS

fake = Faker()


class Command(BaseCommand):
    help = 'Generate Random records'

    def handle(self, *args, **options):
        for index in range(100):
            Faker.seed(index)
            ContactUS.objects.create(
                email_from=fake.ascii_email(),
                subject=fake.sentence(),
                message=fake.text(),
            )
