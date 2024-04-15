from rest_framework import viewsets
from api.models import Match
from api.serializers import MatchSerializer


class MatchViewset(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
