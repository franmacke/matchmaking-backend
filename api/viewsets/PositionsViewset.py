from rest_framework import viewsets, permissions
from api.models import Positions
from api.serializers.PositionsSerializer import PositionsSerializer


class PositionsViewset(viewsets.ModelViewSet):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer

