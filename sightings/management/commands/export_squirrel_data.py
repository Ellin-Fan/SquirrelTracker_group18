import csv
import datetime
from django.core.management.base import BaseCommand
from sightings.models import Sight

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        with open(options['path'][0],'w') as fp:
            fp.write('X,Y,Unique Squirrel ID,Shift,Date,Age,Primary Fur Color,Location,Specific Location,Running,Chasing,Climbing,Eating,Foraging,Other Activities,Kuks,Quaas,Moans,Tail flags,Tail twitches,Approaches,Indifferent,Runs_from\n')
            for row in Sight.objects.all():
                if row.Date: 
                    date_form = row.Date.strftime('%m%d%Y')
                else:
                    date_form = row.Date
                new_line = f"{row.Longitude},{row.Latitude},{row.Unique_Squirrel_Id},{row.Shift},{date_form},{row.Age},{row.Primary_Fur_Color},{row.Location},{row.Specific_Location},{row.Running},{row.Chasing},{row.Climbing},{row.Eating},{row.Foraging},{row.Other_Activities},{row.Kuks},{row.Quaas},{row.Moans},{row.Tail_Flags},{row.Tail_Twitches},{row.Approaches},{row.Indifferent},{row.Runs_From},\n"
                fp.write(new_line)
