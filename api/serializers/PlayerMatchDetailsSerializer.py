from rest_framework import serializers
from api.models import PlayerMatchDetails
from api.serializers.PlayerSerializer import PlayerSerializer
from api.serializers.MatchSerializer import MatchSerializer

class PlayerMatchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerMatchDetails
        fields = '__all__'


class PlayerMatchDetailsGetSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    match = MatchSerializer()

    class Meta:
        model = PlayerMatchDetails
        fields = '__all__'