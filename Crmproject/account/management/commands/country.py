import django
import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','MedicalTourism.settings')
from django.core.management.base import BaseCommand, CommandError
from account.models import Country,State
django.setup()



class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('Country.txt') as jsonfile:
            data = json.load(jsonfile)
            for d in data :
                Country.objects.get_or_create(name=d['country_name'], country_code=d['sortname'])
                for s in d['states'] :
                    State.objects.get_or_create(name=s['state_name'], country_id=Country.objects.get(id=s['country_id']))
               


