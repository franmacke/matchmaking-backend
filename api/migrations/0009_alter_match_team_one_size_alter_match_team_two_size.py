# Generated by Django 5.0.4 on 2024-04-24 15:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_matchdetails_playermatchdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='team_one_size',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='team_two_size',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)]),
        ),
    ]
