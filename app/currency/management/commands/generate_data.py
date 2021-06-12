import random

from django.core.management.base import BaseCommand
from currency.models import Rate

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for index in range (100):
            Rate.objects.create(
                currency_name='usd',
                sale=index+1,
                buy=index,
                source=random.choice(('monobank', 'privatbank', 'vkurse'))
            )

