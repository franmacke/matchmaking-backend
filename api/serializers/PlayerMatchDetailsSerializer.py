from rest_framework import serializers
from api.models import PlayerMatchDetails
from api.serializers.PlayerSerializer import PlayerSerializer
from api.serializers.MatchSerializer import MatchSerializer

class PlayerMatchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerMatchDetails
        fields = '__all__'

    def is_user_in_match(self, player, match):
        return PlayerMatchDetails.objects.filter(
            player_id=player, 
            match_id=match
        ).exists()

    def create(self, validated_data):
        if self.is_user_in_match(validated_data['player'], validated_data['match']):
            raise serializers.ValidationError({"message": "Player already exists in this match"})
        return super().create(validated_data)

class PlayerMatchDetailsGetSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    match = MatchSerializer()

    class Meta:
        model = PlayerMatchDetails
        fields = '__all__'