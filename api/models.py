from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Player(models.Model):
    GENDER_CHOICES = (
        (1, 'Masculino'),
        (2, 'Femenino'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    skill = models.FloatField(null=True)

    def __str__(self):
        return self.name

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
    WINNER_CHOICES = (
        (1, 'Equipo 1'),
        (2, 'Equipo 2'),
        (0, 'Empate'),
    )

    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    field_size = models.IntegerField(validators=[MinValueValidator(4), MaxValueValidator(15)])
    team_one_size = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(15)], blank=True, null=True)
    team_two_size = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(15)], blank=True, null=True)
    team_one_goals = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])
    team_two_goals = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])
    goal_difference = models.IntegerField(null=True, validators=[MinValueValidator(-30), MaxValueValidator(30)])
    match_rating = models.FloatField(null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    balanced = models.BooleanField(null=True, choices=BALANCED_CHOICES, blank=True)
    winner = models.IntegerField(null=True, choices=WINNER_CHOICES, blank=True)

    def __str__(self):
        return f'{self.date.strftime("%d/%m/%Y %H:%M")} [{self.team_one_size}vs{self.team_two_size}] -> {self.team_one_goals} - {self.team_two_goals}'


class Positions(models.Model):
    POSITION_CHOICES = (
        (1, 'Portero'),
        (2, 'Defensa'),
        (3, 'Medio'),
        (4, 'Delantero'),
    )

    id = models.AutoField(primary_key=True)
    position = models.IntegerField(null=True, choices=POSITION_CHOICES, blank=True)

    def __str__(self):
        return f'{self.POSITION_CHOICES[self.position - 1][1]}'


class PlayerMatchDetails(models.Model):
    TEAM_CHOICES = (
        (1, 'Equipo 1'),
        (2, 'Equipo 2'),
    )

    match = models.ForeignKey(Match, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)

    team = models.IntegerField(null=True, choices=TEAM_CHOICES, blank=True)

    # OFFENSE STATS
    goals = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])
    assists = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])
    shots_on_target = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])
    total_shots = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])

    # MIDFIELD STATS
    total_passes = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    successful_passes = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(1000)])

    # DEFENSE STATS
    interceptions = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])
    tackles = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])

    # GOALKEEPER STATS
    saves = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])
    goals_conceded = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(30)])

    # PHYSICAL STATS
    distance_index = models.FloatField(null=True)
    speed_index = models.FloatField(null=True)
    endurance_index = models.FloatField(null=True)

    # OVERALL STATS
    positions = models.ManyToManyField(Positions)
    individual_rating = models.FloatField(null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])

    
