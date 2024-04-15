from django.db import models



class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    skill = models.IntegerField()

class Match(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    number_of_players = models.IntegerField()
    team_size = models.IntegerField()
    field_size = models.IntegerField()
    result = models.CharField(max_length=15)
    team_one_goals = models.IntegerField()
    team_two_goals = models.IntegerField()
    goal_difference = models.IntegerField()

class MatchDetails(models.Model):
    match = models.ForeignKey(Match, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    team = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    score = models.IntegerField()

    