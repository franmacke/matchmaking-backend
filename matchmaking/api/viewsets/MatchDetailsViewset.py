from rest_framework import viewsets
from api.models import MatchDetails
from api.serializers import MatchDetailsSerializer


class MatchDetailsViewset(viewsets.ModelViewSet):
    serializer_class = MatchDetailsSerializer
    queryset = MatchDetails.objects.all()
