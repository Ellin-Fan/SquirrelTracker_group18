from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Sight(models.Model):
    Longitude  = models.FloatField(
            help_text = _('Longitude of the sight'),)
    Latitude = models.FloatField(
            help_text = _('Latitude of the sight'),)
    Unique_Squirrel_Id = models.CharField(
            help_text = _('The unique ID of the squirrel'),max_length=25,)
    AM = 'AM'
    PM = 'PM'
    SESSION=(
            (AM,'AM'),
            (PM,'PM'),
            )
    Shift = models.CharField(
            help_text = _('Whether the sight is in the morning or late afternoon?'),
            max_length=16,
            choices=SESSION,)
    Date = models.CharField(
            help_text = _('Date of the sighting'),
            max_length=16)
    Adult = 'Adult'
    Juvenile = 'Juvenile'
    AGE_CHOICE=(
            (Adult,'Adult'),
            (Juvenile, 'Juvenile'),
            (None, '-'),
            )
    Age = models.CharField(
            help_text = _('Age'),
            max_length=16,
            choices = AGE_CHOICE,
            )
    Black = 'Black'
    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    COLOR_CHOICE=(
            (Black, 'Black'),
            (Gray, 'Gray'),
            (Cinnamon, 'Cinnamon'),
            (None, '-'),
            )
    Primary_Fur_Color = models.CharField(
            help_text = _('Fur color'),
            max_length=16,
            choices = COLOR_CHOICE,
            )
    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'
    LOCATION_CHOICE=(
            (Ground_Plane, 'Ground Plane'),
            (Above_Ground, 'Above Ground'),
            (None, '-'),
            )
    Location =  models.CharField(
            help_text = _('Location'),
            max_length=128,
            choices = LOCATION_CHOICE,
            )
    Specific_Location = models.CharField(
            help_text = _('Additional notes to the location'),
            max_length=128,
            blank = True,)
    Running = models.BooleanField()
    Chasing = models.BooleanField()
    Climbing = models.BooleanField()
    Eating = models.BooleanField()
    Foraging = models.BooleanField()
    Other_Activities = models.CharField(
            max_length=128,
            blank = True,)
    Kuks = models.BooleanField()
    Quaas = models.BooleanField()
    Moans = models.BooleanField()
    Tail_flags = models.BooleanField()
    Tail_twitches = models.BooleanField()
    Approaches = models.BooleanField()
    Indifferent = models.BooleanField()
    Runs_from = models.BooleanField()
