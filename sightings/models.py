from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Sight(models.Model):
    Longitude  = models.FloatField(
            help_text = _('Longitude of the sight'),)

    Latitude = models.FloatField(
            help_text = _('Latitude of the sight'),)

    Unique_Squirrel_Id = models.CharField(
            help_text = _('The unique ID of the squirrel'),
            max_length = 25,
            )
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

    Date = models.IntegerField(
            help_text = _('Date of the sighting'),
            null = True,)

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Unknown = '?'
    AGE_CHOICE=(
            (Adult,'Adult'),
            (Juvenile, 'Juvenile'),
            (None, '-'),
            (Unknown, '?'),
            )

    Age = models.CharField(
            help_text = _('Age of the squirrel'),
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
            blank = True,
            )

    TRUE = 'TRUE'
    FALSE = 'FALSE'

    BOOLEAN_CHOICES = (
            (TRUE,'True'),
            (FALSE,'False'),
            )

    Running = models.CharField(
            help_text = _('Running'),
            choices=BOOLEAN_CHOICES,
            default=FALSE,
            max_length=16,
            null=True,
    )
    Chasing = models.CharField(
            help_text = _('Chasing'),
            choices=BOOLEAN_CHOICES,
            default=FALSE,
            max_length=16,
            null=True,
    )
    Climbing = models.CharField(
            help_text = _('Climbing'),
            choices=BOOLEAN_CHOICES,
            default=FALSE,
            max_length=16,
            null=True,
    )
    Eating = models.CharField(
            help_text = _('Eating'),
            choices=BOOLEAN_CHOICES,
            default=FALSE,
            max_length=16,
            null=True,
    )
    Foraging = models.CharField(
            help_text = _('Foraging'),
            choices=BOOLEAN_CHOICES,
            default=FALSE,
            max_length=16,
            null=True,
    )

    Other_Activities = models.CharField(

        help_text = _('Other Activities'),
        max_length = 128,
        null = True,
    )
    Kuks = models.CharField(
            help_text = _('Kuks'),
            choices=BOOLEAN_CHOICES,
            default=FALSE,
            max_length=16,
            null=True,
    )
    Quaas = models.CharField(
            help_text = _('Quaas'),
            choices=BOOLEAN_CHOICES,
            default=FALSE,
            max_length=16,
            null=True,
    )
    Moans = models.CharField(
            help_text = _('Moans'),
            choices=BOOLEAN_CHOICES,
            default=FALSE,
            max_length=16,
            null=True,
    )
    Tail_Flags = models.CharField(
            help_text = _('Tail_Flags'),
            choices=BOOLEAN_CHOICES,
            default=FALSE,
            max_length=16,
            null=True,
    )
    Tail_Twitches = models.CharField(
            help_text = _('Tail_Twiches'),
            choices=BOOLEAN_CHOICES,
            default=FALSE,
            max_length=16,
            null=True,
    )
    Approaches = models.CharField(
            help_text = _('Approaches'),
            choices=BOOLEAN_CHOICES,
            default=FALSE,
            max_length=16,
            null=True,
    )
    Indifferent = models.CharField(
            help_text = _('Indifferent'),
            choices=BOOLEAN_CHOICES,
            default=FALSE,
            max_length=16,
            null=True,
    )
    Runs_From = models.CharField(
            help_text = _('Runs_From'),
            choices=BOOLEAN_CHOICES,
            default=FALSE,
            max_length=16,
            null=True,
    )

