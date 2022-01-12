import csv
from django.core.management.base import BaseCommand
from recipes.models import Ingredient

DATA_PATH = 'data/'


class Command(BaseCommand):

    help = 'Import data from project CSV files'

    def handle(self, *args, **options):
        with open(DATA_PATH + 'ingredients.csv',
                  mode="r", encoding="utf-8") as f_obj:
            reader = csv.reader(f_obj)
            for row in reader:
                if len(row) == 2:
                    Ingredient.objects.get_or_create(name=row[0],
                                                     measurement_unit=row[1])
                print(row)
