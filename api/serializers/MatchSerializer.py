from rest_framework import serializers
from api.models import Match

class MatchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Match
        fields = '__all__'

    def define_winner(self, team_one_goals, team_two_goals):
        if not team_one_goals or not team_two_goals:
            return None
        if team_one_goals > team_two_goals:
            return 1
        if team_one_goals < team_two_goals:
            return 2
        return 0
    
    def calculate_goal_difference(self, team_one_goals, team_two_goals):
        return None if not team_one_goals or not team_two_goals else team_one_goals - team_two_goals


    def calculate_number_of_players(self, team_one_size, team_two_size):
        if not team_one_size or not team_two_size:
            return None
        return team_one_size + team_two_size


    def create(self, validated_data):

        team_one_goals = validated_data.get('team_one_goals', None)
        team_two_goals = validated_data.get('team_two_goals', None)

        match = Match.objects.create(
            date=validated_data['date'],
            field_size=validated_data['field_size'],

            # OPTIONAL
            team_one_size=validated_data.get('team_one_size', None),
            team_two_size=validated_data.get('team_two_size', None),
            team_one_goals=team_one_goals,
            team_two_goals=team_two_goals,
            goal_difference=self.calculate_goal_difference(team_one_goals, team_two_goals),
            match_rating=validated_data.get('match_rating', None),
            balanced=validated_data.get('balanced', None),
            winner=self.define_winner(team_one_goals, team_two_goals)
        )

        return match

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.field_size = validated_data.get('field_size', instance.field_size)
        
        instance.team_one_size = validated_data.get('team_one_size', instance.team_one_size)
        instance.team_two_size = validated_data.get('team_two_size', instance.team_two_size)
        instance.team_one_goals = validated_data.get('team_one_goals', instance.team_one_goals)
        instance.team_two_goals = validated_data.get('team_two_goals', instance.team_two_goals)
        instance.goal_difference = self.calculate_goal_difference(instance.team_one_goals, instance.team_two_goals)
        instance.match_rating = validated_data.get('match_rating', instance.match_rating)
        instance.balanced = validated_data.get('balanced', instance.balanced)
        instance.winner = self.define_winner(instance.team_one_goals, instance.team_two_goals)

        instance.save()
        return instance

