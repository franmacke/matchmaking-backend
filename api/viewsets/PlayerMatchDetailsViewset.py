from rest_framework import viewsets
from api.models import PlayerMatchDetails
from api.serializers import PlayerMatchDetailsSerializer,PlayerMatchDetailsGetSerializer


class PlayerMatchDetailsViewset(viewsets.ModelViewSet):

    queryset = PlayerMatchDetails.objects.all()

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return PlayerMatchDetailsSerializer
        return PlayerMatchDetailsGetSerializer


