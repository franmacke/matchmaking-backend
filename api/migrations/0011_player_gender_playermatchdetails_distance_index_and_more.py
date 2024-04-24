# Generated by Django 5.0.4 on 2024-04-24 16:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_match_number_of_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='gender',
            field=models.CharField(choices=[(1, 'Masculino'), (2, 'Femenino')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playermatchdetails',
            name='distance_index',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='playermatchdetails',
            name='endurance_index',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='playermatchdetails',
            name='goals_conceded',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AddField(
            model_name='playermatchdetails',
            name='interceptions',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AddField(
            model_name='playermatchdetails',
            name='saves',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AddField(
            model_name='playermatchdetails',
            name='shots_on_target',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AddField(
            model_name='playermatchdetails',
            name='speed_index',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='playermatchdetails',
            name='successful_passes',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='playermatchdetails',
            name='tackles',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AddField(
            model_name='playermatchdetails',
            name='total_passes',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
        ),
        migrations.AddField(
            model_name='playermatchdetails',
            name='total_shots',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)]),
        ),
    ]