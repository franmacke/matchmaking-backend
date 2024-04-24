# Generated by Django 5.0.4 on 2024-04-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_match_number_of_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('position', models.IntegerField(blank=True, choices=[(1, 'Portero'), (2, 'Defensa'), (3, 'Medio'), (4, 'Delantero')], null=True)),
            ],
        ),
        migrations.AddField(
            model_name='matchdetails',
            name='positions',
            field=models.ManyToManyField(to='api.positions'),
        ),
    ]