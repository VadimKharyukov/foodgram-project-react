import csv

from django.core.management.base import BaseCommand

from recipes.models import Tag

DATA_PATH = 'data/'


class Command(BaseCommand):

    help = 'Import data from project CSV files'

    def handle(self, *args, **options):
        with open(DATA_PATH + 'tags.csv',
                  mode="r", encoding="utf-8") as f_obj:
            reader = csv.reader(f_obj)
            for row in reader:
                if len(row) == 3:
                    Tag.objects.get_or_create(name=row[0],
                                              color=row[1], slug=row[2])
                print(row)
