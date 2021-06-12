import random

from django.core.management.base import BaseCommand
from currency.models import Rate


class Command(BaseCommand):
    help = 'Generate Random records'

    def handle(self, *args, **options):
        for index in range(100):
            Rate.objects.create(
                currency_name=random.choice(('usd', 'eur')),
                sale=random.uniform(20.00, 29.99),
                buy=random.uniform(20.00, 29.99),
                source=random.choice(('monobank', 'privatbank', 'vkurse'))
            )
