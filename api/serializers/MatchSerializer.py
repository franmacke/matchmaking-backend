from rest_framework import serializers
from api.models import Match

class MatchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Match
        fields = '__all__'

    def define_winner(self, team_one_goals, team_two_goals):
        if team_one_goals > team_two_goals:
            return 1
        if team_one_goals < team_two_goals:
            return 2
        return 0

    def create(self, validated_data):

        match = Match.objects.create(
            date=validated_data['date'],
            number_of_players=validated_data['team_one_size'] + validated_data['team_two_size'],
            team_one_size=validated_data['team_one_size'],
            team_two_size=validated_data['team_two_size'],
            field_size=validated_data['field_size'],
            team_one_goals=validated_data['team_one_goals'],
            team_two_goals=validated_data['team_two_goals'],
            goal_difference=validated_data['team_one_goals'] - validated_data['team_two_goals'],
            match_rating=validated_data['match_rating'],
            balanced=validated_data['balanced'],
            winner=self.define_winner(validated_data['team_one_goals'], validated_data['team_two_goals'])
        )

        return match
