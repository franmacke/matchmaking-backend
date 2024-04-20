from rest_framework import viewsets
from api.models import MatchDetails
from api.serializers import MatchDetailsSerializer
from rest_framework.response import Response


class MatchDetailsViewset(viewsets.ModelViewSet):
    queryset = MatchDetails.objects.all()
    serializer_class = MatchDetailsSerializer
