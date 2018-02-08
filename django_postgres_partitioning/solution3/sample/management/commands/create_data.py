import random
import string
from django.core.management.base import BaseCommand, CommandError
from sample.models import Sample1


class Command(BaseCommand):
    help = 'Create random data'

    def add_arguments(self, parser):
        parser.add_argument('data_size', type=int)

    def handle(self, *args, **options):
        for i in range(0, options['data_size']):
            sample = Sample1()
            sample.name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50))
            sample.description = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(200))
            sample.save()
