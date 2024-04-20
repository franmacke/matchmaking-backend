from rest_framework import serializers
from api.models import PlayerMatchDetails

class PlayerMatchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerMatchDetails
        fields = '__all__'
