from rest_framework import viewsets
from api.models import PlayerMatchDetails
from api.serializers.PlayerMatchDetailsSerializer import PlayerMatchDetailsSerializer


class PlayerMatchDetailsViewset(viewsets.ModelViewSet):
    queryset = PlayerMatchDetails.objects.all()
    serializer_class = PlayerMatchDetailsSerializer
