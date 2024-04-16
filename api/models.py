from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    skill = models.FloatField(null=True)

class Match(models.Model):
    RESULT_CHOICES = (
        (1, 'Vitoria'),
        (0, 'Empate'),
        (-1, 'Derrota'),
    )
    BALANCED_CHOICES = (
        (True, 'Balanceado'),
        (False, 'Desbalanceado'),
    )

    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    number_of_players = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    team_size = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(15)])
    field_size = models.IntegerField(validators=[MinValueValidator(4), MaxValueValidator(15)])
    result = models.CharField(max_length=15, null=True, choices=RESULT_CHOICES, blank=True)
    team_one_goals = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])
    team_two_goals = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])
    goal_difference = models.IntegerField(null=True, validators=[MinValueValidator(-30), MaxValueValidator(30)])
    match_rating = models.FloatField(null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    balanced = models.BooleanField(null=True, choices=BALANCED_CHOICES, blank=True)

class MatchDetails(models.Model):
    TEAM_CHOICES = (
        (1, 'Equipo 1'),
        (2, 'Equipo 2'),
    )

    match = models.ForeignKey(Match, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    team = models.IntegerField(null=True, choices=TEAM_CHOICES, blank=True)
    goals = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])
    assists = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])
    individual_rating = models.FloatField(null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])

    