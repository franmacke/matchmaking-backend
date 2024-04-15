from rest_framework.viewsets import ModelViewSet
from api.models import Player
from api.serializers import PlayerSerializer

class PlayerViewset(ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()