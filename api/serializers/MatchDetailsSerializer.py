from rest_framework import serializers
from api.models import MatchDetails

class MatchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDetails
        fields = '__all__'
