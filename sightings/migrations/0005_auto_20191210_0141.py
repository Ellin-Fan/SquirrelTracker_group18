# Generated by Django 3.0 on 2019-12-10 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0004_auto_20191208_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sight',
            name='Age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), (None, ''), ('?', '?')], help_text='Age of the squirrel', max_length=16),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Location',
            field=models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground'), (None, '')], help_text='Location', max_length=128),
        ),
        migrations.AlterField(
            model_name='sight',
            name='Primary_Fur_Color',
            field=models.CharField(blank=True, choices=[('Black', 'Black'), ('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), (None, '')], help_text='Fur color', max_length=16),
        ),
    ]