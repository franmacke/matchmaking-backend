from rest_framework import viewsets
from api.models import MatchDetails
from api.serializers import MatchDetailsSerializer


class MatchDetailsViewset(viewsets.ModelViewSet):
    queryset = MatchDetails.objects.all()
    serializer_class = MatchDetailsSerializer